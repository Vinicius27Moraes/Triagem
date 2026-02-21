from cx_Freeze import setup, Executable

# Informações do seu script
script = "Interface.py"  # Substitua pelo nome do seu script Python
executables = [Executable(script)]

setup(
    name="ENCAMINHAMENTO",
    version="0.1",
    description="Encaminhamento dos chamados.",
    executables=executables
)
