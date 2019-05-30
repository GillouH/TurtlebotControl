#!/usr/bin/env python3
# -*-coding:utf-8 -*


class OrderedDictionary:
	def __init__(self, base={}, **donnees):
		self._cles = []
		self._valeurs = []

		if type(base) not in (dict, OrderedDictionary):
			raise TypeError("le type attendu est un dictionnaire (usuel ou ordonne)")
		for cle in base.keys():
			self[cle] = base[cle]
		for cle in donnees.keys():
			self[cle] = donnees[cle]

	def __repr__(self):
		string = "{"
		for key, value in self.items():
			string += str(key) + " : " + str(value) + ", "
		string = string[:-2]
		string += "}"
		return string
	def __str__(self):
		return repr(self)

	def __len__(self):
		return len(self._cles)

	def __contains__(self, cle):
		return cle in self._cles

	def __getitem__(self, cle):
		if cle not in self._cles:
			raise KeyError("La clé {0} ne se trouve pas dans le dictionnaire".format(cle))
		else:
			indice = self._cles.index(cle)
			return self._valeurs[indice]

	def __setitem__(self, cle, valeur):
		if cle in self._cles:
			indice = self._cles.index(cle)
			self._valeurs[indice] = valeur
		else:
			self._cles.append(cle)
			self._valeurs.append(valeur)

	def __delitem__(self, cle):
		if cle not in self._cles:
			raise KeyError("La clé {0} ne se trouve pas dans le dictionnaire".format(cle))
		else:
			indice = self._cles.index(cle)
			del self._cles[indice]
			del self._valeurs[indice]

	def __iter__(self):
		"""Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
		return iter(self._cles)

	def items(self):
		"""Renvoie un générateur contenant les couples (cle, valeur)"""
		for i, cle in enumerate(self._cles):
			valeur = self._valeurs[i]
			yield (cle, valeur)

	def keys(self):
		"""Cette méthode renvoie la liste des clés"""
		return list(self._cles)

	def values(self):
		"""Cette méthode renvoie la liste des valeurs"""
		return list(self._valeurs)


if __name__ == '__main__':
	pass
