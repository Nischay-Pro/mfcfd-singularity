import subprocess

def main():
    spack = open("/root/.spack/linux/compilers.yaml").read()

    nvhpc_path = getApplicationOutput(["/opt/spack/bin/spack", "location", "-i", "nvhpc@21.2"]).split("\n")[0]

    data = open("/root/compiler.template").read()
    data = data.replace("{{PATH}}", nvhpc_path)
    data = spack + data
    with open("/root/.spack/linux/compilers.yaml", 'w') as f:
        f.write(data)

def getApplicationOutput(command, shell=False):
    return subprocess.run(command, shell=shell, check=True, universal_newlines=True,
                          stdout=subprocess.PIPE).stdout

if __name__ == "__main__":
    main()