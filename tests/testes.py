class Structure():
    def __init__(self, name, type, sequence):
        self.name = name
        self.type = type
        self.sequence = sequence

    def __str__(self):
        return self.name + ' ' + self.type + ' ' + self.sequence

    def __repr__(self):
        return self.name + ' ' + self.type + ' ' + self.sequence

estrutura = Structure('Estrutura', 'DNA', 'gugugugucaucgaucgu')
print(estrutura)


# uguuauauucaaaauuguccucuuggu CYIQNCPLG
# uguuauuuucaaaauuguccucguggu CYFQNCPRG

# uguuauauucaaaauuguccucuugguugaccgggcauguguuauuuucaaaauuguccucguggu