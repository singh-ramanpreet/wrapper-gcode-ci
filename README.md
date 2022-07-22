# wrapper-gcode-ci
CI for generating Wrapper G-code

## How this works?

- Any changes to `.py` and `.yml` files will trigger [GitHub Actions](https://github.com/singh-ramanpreet/wrapper-gcode-ci/actions).
- Python script `generate.py` using `config.yml` will generate G-Code for different tile sizes.
- Generated G-Code will be committed to this `main` branch by [GitHub Actions](https://github.com/singh-ramanpreet/wrapper-gcode-ci/actions), if there are changes.

## How to download generated G-Code?

Use PowerShell script `download-gcode.ps1` to download `R*.PIT` files to PC connected to machine.`

1. Get the PS Script. Skip this step if you have it already. Right-Click [download](https://raw.githubusercontent.com/singh-ramanpreet/wrapper-gcode-ci/main/download-gcode.ps1)
 link and select `Save As`. Make sure file extension is `.ps1`.
2. Run the Script. Right-Click the downloaded script, select `Run With PowerShell`. Select the destination folder and press `Ok`.

## Development

1. Add keys like `R18-19` in `config.yml` for additional sizes code generation.
2. Specify param for tile size differing from default in `config.yml`.
3. Look for defaults in `generate.py`, like `pc.set(<param>, <default>)`. Use this same syntax to add more params.

## Tags:

- `v2.0`: With additional steps of applying pressure with foam after the sticker application.
- `v1.0`: Initial version.
