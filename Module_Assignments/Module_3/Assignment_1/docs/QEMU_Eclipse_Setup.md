# Day 1 — QEMU Setup + Eclipse/GDB Debugging (Embedded Platform Simulation)

Goal: replace the physical embedded board with a QEMU-emulated equivalent, and
wire up Eclipse + GDB so you can still do source-level debugging of the
firmware/application running "on the board" — even though it's virtual.

> Substitute your actual board/CPU/image names below — this is written for a
> generic ARM Cortex-A/Linux-capable target, which is the most common case
> for "embedded platform simulation" assignments. If your target is a
> microcontroller (Cortex-M / bare-metal), see the note at the end.

---

## Step 1 — Install QEMU

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install qemu-system-arm qemu-system-x86 gdb-multiarch
```

**Windows:** download the installer from https://www.qemu.org/download/ and
add the install directory to PATH.

**macOS:**
```bash
brew install qemu
```

Verify:
```bash
qemu-system-arm --version
```

---

## Step 2 — Get/Build the target image

You need three things for the emulated board:
1. A kernel image (e.g. `zImage` or `Image`)
2. A device tree blob (`.dtb`) matching the board QEMU is emulating
3. A root filesystem image (e.g. `rootfs.ext4` or an `.img`)

If your course provides a pre-built image, place it in `~/embedded/` and skip
to Step 3. Otherwise, a common quick-start is Buildroot:
```bash
git clone https://github.com/buildroot/buildroot.git
cd buildroot
make qemu_arm_versatile_defconfig
make -j$(nproc)
# Output: output/images/{zImage, rootfs.ext2, versatile-pb.dtb}
```

---

## Step 3 — Boot the target under QEMU (with a GDB stub enabled)

```bash
qemu-system-arm \
  -M versatilepb \
  -kernel output/images/zImage \
  -dtb output/images/versatile-pb.dtb \
  -drive file=output/images/rootfs.ext2,if=scsi,format=raw \
  -append "root=/dev/sda console=ttyAMA0" \
  -net nic -net user,hostfwd=tcp::8080-:80 \
  -nographic \
  -s -S
```

Key flags:
- `-s` → shorthand for `-gdb tcp::1234` (starts a GDB server on port 1234)
- `-S` → freeze the CPU at startup so GDB can attach *before* anything runs
- `-net user,hostfwd=tcp::8080-:80` → forwards host port **8080** to port 80
  inside the emulated target. This is the port your Selenium/Behave suite
  will hit as `BASE_URL=http://localhost:8080` instead of a real device IP.

Adjust `-M` (machine type) and the forwarded port to match whatever
service/UI your embedded app actually exposes.

---

## Step 4 — Configure Eclipse with GDB for debugging

1. Install **Eclipse IDE for Embedded C/C++ Developers** (or Eclipse CDT +
   the "C/C++ GDB Hardware Debugging" plugin via Help → Install New Software).
2. Import your firmware/application source as a C/C++ project
   (File → Import → Existing Code as Makefile Project).
3. Open **Run → Debug Configurations → GDB Hardware Debugging** → New
   configuration:
   - **Main tab:** point "C/C++ Application" at the compiled ELF binary
     (the unstripped build with debug symbols, e.g. `vmlinux` or your app's
     `.elf`).
   - **Debugger tab:**
     - GDB command: `gdb-multiarch` (Linux) or the cross-gdb for your target
       triple (e.g. `arm-none-eabi-gdb`)
     - Use remote target: ✅
     - JTAG Device: **Generic TCP/IP**
     - Host: `localhost`, Port: `1234` (matches QEMU's `-s` flag from Step 3)
4. Click **Debug**. Eclipse connects to QEMU's GDB stub, halts at the entry
   point (because we passed `-S`), and you can now set breakpoints, step
   through source, inspect variables/registers — exactly as if attached to
   real hardware via JTAG.
5. Press **Resume** in Eclipse (or `continue` in the GDB console) to let the
   emulated system finish booting.

---

## Step 5 — Confirm the simulated environment is reachable

Once booted, confirm the forwarded port responds before pointing Behave at it:
```bash
curl http://localhost:8080/
```

Then, for Days 2–4, set:
```bash
export BASE_URL="http://localhost:8080"
behave
```

Your existing feature files and step definitions run unchanged — Selenium is
simply driving a browser against a URL that happens to be served by an
emulator instead of a physical board.

---

## Note: bare-metal / microcontroller targets

If your "embedded platform" is a microcontroller (no OS, no HTTP interface —
e.g. an STM32/Cortex-M target) rather than a Linux-capable SoC:
- Use `qemu-system-gnuarmeclipse` or Renode instead of vanilla QEMU (better
  peripheral/microcontroller support).
- There's typically no web UI to point Selenium at directly — in that case,
  Day 2–4 "end-to-end scenarios" usually mean driving a **serial/UART or
  REST bridge** that QEMU/Renode exposes on the host, and your Behave step
  definitions would use `pyserial` or `requests` instead of Selenium's
  browser driver for the parts that talk to the target. Selenium still
  covers any web dashboard/UI layered on top, if one exists.
