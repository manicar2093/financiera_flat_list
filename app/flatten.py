def flatten(data: list, target:list = None):
	"""Crea una versión flat de la lista que se reciba. La lista recibida puede estar anidada x numero de veces. Si el target es una lista de listas, esta no será procesada y se regresará una lista de listas. Por ejemplo:

	data = [[[4,5,6],7],8]
	target = [[1,2,3]]
	resultado = [[1,2,3],4,5,6,7,8]

	Args:
		data (list): Lista que se necesita hacer flat
		target (list, optional): Recibe una lista en donde se desee colocar los datos ya procesados. Si no se recibe se crea una lista vacia. Defaults to None.

	Returns:
		[list]: Lista con los datos procesados
	"""
	if target is None:
		target = []
	if type(target) is not list:
		raise TypeError("El target no es una lista")
	for item in data:
		if type(item) is list:
			flatten(item, target)
		else:
			target.append(item)
	return target