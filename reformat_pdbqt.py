import sys

inp, outp = sys.argv[1], sys.argv[2]

with open(inp) as f, open(outp, "w") as g:
    for line in f:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            serial = int(line[6:11])
            name   = line[12:16]
            resn   = line[17:20]
            resi   = int(line[22:26])
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            q = float(line[54:62])
            atype = line[77:].strip()
            g.write(f"ATOM  {serial:5d} {name:<4}{resn:>3}  {resi:4d}    "
                    f"{x:8.3f}{y:8.3f}{z:8.3f}{q:7.3f} {atype:>2}\n")
        else:
            g.write(line)
