import unittest
from app.flatten import flatten

class TestFlattenFunc(unittest.TestCase):

    def test_flatten_succes(self):
        """Valida el happy path de la función"""
        expect = [1,2,3,4,5]
        got = flatten(data=[1, [2, [3, [4, 5]]]])
        self.assertListEqual(expect, got, "Listas no son iguales")

    def test_flatten_data_wrong_type(self):
        """Valida que levante una excepción TypeError cuando el dato que se quiere procesar no es una lista"""
        with self.assertRaises(TypeError):
            flatten(data=4)
    
    def test_flatten_many_data(self):
        """Realiza la prueba de varias listas"""
        table_test = [
            {"expect":[1,2,3,4,5,6,7,8], "data":[1,[2,[3,[4,5,[6]],7,8]]], "target":[]},
            {"expect":[1,2,3,4,5,6,7,8], "data":[[4,5,[6]],7,8], "target":[1,2,3]},
            {"expect":[1,2,3,4,5,6,7,8], "data":[1,[2,[3,4,5,[6],7,8]]], "target":None},
            {"expect":[[1,2,3],4,5,6,7,8], "data":[[[4,5,6],7],8], "target":[[1,2,3]]},
            {"expect":[[1,2,3],[4],5,6,7,8], "data":[[[5,6],7],8], "target":[[1,2,3],[4]]},
        ]

        for test in table_test:
            got = flatten(data=test["data"], target=test["target"])
            self.assertListEqual(got, test["expect"], "Listas no son iguales")

    def test_flatten_with_target(self):
        """Valida que cuando se mande una lista target se agregue la info correctamente"""
        target = [1,2,3]
        expect = [1,2,3,4,5,6,7,8,9]

        got = flatten(data=[4,[5,[6],7],8,[9]], target=target)

        self.assertListEqual(got, expect, "Listas no son iguales")

    def test_flatten_with_target_not_a_list(self):
        """Valida se levante error TypeError cuando el target no es una lista"""
        target = "target"
        
        with self.assertRaises(TypeError):
            flatten(data=[4,[5,[6],7],8,[9]], target=target)
        
