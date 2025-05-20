# #!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='Mutt'):
        self.name=name
        self.breed=breed
        print(f"{name} is a {breed}")


fido=Dog('Bosco')
fido=Dog('Bosco','German Shepherd')


# fido =Dog('Fido')
# snoopy=Dog('Snoopy')
# print(fido.name)
# fido.owner="sophie"
# print(fido.owner)

# class Dog:
#     def showing_self(self):
#         return self
    
# fido=Dog()
# print(fido.showing_self())
# print(fido is fido.showing_self())
