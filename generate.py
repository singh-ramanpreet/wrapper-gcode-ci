from yaml import load, Loader


class program_config:
    def __init__(self, config: dict) -> None:
        self.config = config

    def set(self, param: str, default: str) -> str:
        if self.config is None:
            return default

        if param in self.config:
            return self.config[param]
        else:
            return default


if __name__ == '__main__':
    # load the yaml data
    data = load(open("config.yml"), Loader=Loader)

    # get list of programs to generate
    progs = list(data.keys())

    for prog in progs:

        pc = program_config(data[prog])

        with open(f"{prog}.PIT", "w") as file:
            file.write(f"%Tile Size {prog.lstrip('R')},MX---,\r\n")
            file.write(f"%,MX---,\r\n")
            file.write(f"(MSG \"START\")\r\n")
            file.write(f"N100 G00 X475 Y520 Z100".ljust(36) + f"; Home position\r\n")
            file.write(f"G00 X632.312 Y816.098 Z63.0".ljust(36) + f"; Move to esr pickup\r\n")
            file.write(f"G01 Z22.240 F2000".ljust(36) + f"; Move down slowly to pickup esr\r\n")
            file.write(f"M1100".ljust(36) + f"; Activating end effector suction\r\n")
            file.write(f"G4K020".ljust(36) + f"; Pause 200 ms to allow vacuum pickup\r\n")
            file.write(f"G00 Z80".ljust(36) + f"; Move up after picking up esr\r\n")
            file.write(f"G00 {pc.set('esr-place','X466.176 Y516.588')} Z25.0".ljust(36) + f"; Move to folding station\r\n")
            file.write(f"G01 Z-3.911 F2000".ljust(36) + f"; Move down esr to folding station\r\n")
            file.write(f"M1101 M1000".ljust(36) + f"; Activating hold down suction and Release end effector\r\n")
            file.write(f"G4K010".ljust(36) + f"; Pause 100 ms\r\n")
            file.write(f"G00 Z35.0".ljust(36) + f"; Move up after placing esr down\r\n")
            file.write(f"M2100".ljust(36) + f"; Activate tile feeder\r\n")
            file.write(f"G4K020".ljust(36) + f"; Pause 200 ms\r\n")
            file.write(f"G00 {pc.set('tile-pick', 'XY')}".ljust(36) + f"; Move to the tile pick up position \r\n")
            file.write(f"G01 Z24.150 F2000".ljust(36) + f"; Move down Z to pickup tile \r\n")
            file.write(f"M1100".ljust(36) + f"; Activating end effector suction\r\n")
            file.write(f"G4K020".ljust(36) + f"; Pause 200 ms\r\n")
            file.write(f"M2000".ljust(36) + f"; Retract tile feeder\r\n")
            file.write(f"G00 Z100.0".ljust(36) + f"; Lift up tile\r\n")
            file.write(f"G00 {pc.set('tile-place', 'X477.014 Y521.774')} Z8.00".ljust(36) + f"; Move back to center to place tile\r\n")
            file.write(f"G01 Z-0.675 F2000".ljust(36) + f"; Move down slowly to place tile\r\n")
            file.write(f"M1000".ljust(36) + f"; Turn off end effector\r\n")
            file.write(f"G01 Z-4.045 F1000 M2101".ljust(36) + f"; Retract folding pocket and push with end effector\r\n")
            file.write(f"G4K010".ljust(36) + f"; Pause 100 ms\r\n")
            file.write(f"G00 Z140.0".ljust(36) + f"; Move up in Z\r\n")
            file.write(f"M2105".ljust(36) + f"; Turn on actuators arm 4\r\n")
            file.write(f"G4K200".ljust(36) + f"; Pause 2000 ms\r\n")
            file.write(f"M2103".ljust(36) + f"; Turn on actuators arm 2\r\n")
            file.write(f"G4K100".ljust(36) + f"; Pause 1000 ms\r\n")
            file.write(f"M2102 M2104".ljust(36) + f"; Turn on actuators 1 and 3\r\n")
            file.write(f"G4K100".ljust(36) + f"; Pause 1000 ms\r\n")
            file.write(f"G00 Y625.619".ljust(36) + f"; Move to sticker\r\n")
            file.write(f"G00 X623.000".ljust(36) + f"; Move to sticker\r\n")
            file.write(f"G01 Z121.041 F1000".ljust(36) + f"; Move to sticker\r\n")
            file.write(f"G4K050".ljust(36) + f"; Pause 500 ms\r\n")
            file.write(f"M1100".ljust(36) + f"; Activating end effector suction\r\n")
            file.write(f"G4K050".ljust(36) + f"; Pause 500 ms\r\n")
            file.write(f"G01 Z125.0 F2000".ljust(36) + f"; Move up to lift sticker\r\n")
            file.write(f"G00 {pc.set('sticker-x-place', 'X478.238')}".ljust(36) + f"; Return to center\r\n")
            file.write(f"G00 {pc.set('sticker-y-place', 'Y522.180')} Z10.0".ljust(36) + f"; Return to center\r\n")
            file.write(f"G01 Z-4.845 F1000".ljust(36) + f"; Apply sticker\r\n")
            file.write(f"M1000".ljust(36) + f"; Release sticker\r\n")
            file.write(f"G4K020".ljust(36) + f"; Pause 200 ms\r\n")
            file.write(f"G00 Z80".ljust(36) + f";\r\n")
            file.write(f"G00 X577.806 Y392.740".ljust(36) + f";\r\n")
            file.write(f"G00 Z27.000".ljust(36) + f";\r\n")
            file.write(f"M1100".ljust(36) + f"; Activating end effector suction\r\n")
            file.write(f"G00 Z80".ljust(36) + f";\r\n")
            file.write(f"G00 X477.014 Y521.774 Z8.00".ljust(36) + f";\r\n")
            file.write(f"G01 Z-3.500 F1000".ljust(36) + f";\r\n")
            file.write(f"G4K200".ljust(36) + f"; Pause 2000 ms\r\n")
            file.write(f"G00 Z80".ljust(36) + f";\r\n")
            file.write(f"G00 X577.806 Y392.740".ljust(36) + f";\r\n")
            file.write(f"G00 Z27.000".ljust(36) + f";\r\n")
            file.write(f"M1000".ljust(36) + f";\r\n")
            file.write(f"G00 Z80".ljust(36) + f";\r\n")
            file.write(f"G00 X477.014 Y521.774 Z10.00".ljust(36) + f";\r\n")
            file.write(f"M2002 M2003 M2004 M2005".ljust(36) + f"; Retract actuators\r\n")
            file.write(f"G00 Z10".ljust(36) + f"; Move up to push out tile\r\n")
            file.write(f"M2001".ljust(36) + f"; Push out pocket\r\n")
            file.write(f"G01 Z0.8 F1000".ljust(36) + f"; Move down to pick up completed tile\r\n")
            file.write(f"M1001".ljust(36) + f"; Release pocket suction\r\n")
            file.write(f"M1100".ljust(36) + f"; Activating end effector\r\n")
            file.write(f"G4K020".ljust(36) + f"; Pause 200 ms for pickup\r\n")
            file.write(f"G00 Z50".ljust(36) + f"; Lift tile\r\n")
            file.write(f"G00 X560.5 Y640.5".ljust(36) + f"; Move to drop of completed tile\r\n")
            file.write(f"M1000".ljust(36) + f"; Release end effector\r\n")
            file.write(f"G00 X475 Y520 Z100".ljust(36) + f"; Return to home position\r\n")
            file.write(f"(MSG \"END\")\r\n")
            file.write(f";(GOTO N100)\r\n")
            file.write(f"M30\r\n")
