import unittest
from final_definitions.volleyball_definitions import InvalidNameException as n
from final_definitions.volleyball_definitions import InvalidPositionException as pos
from final_definitions.volleyball_definitions import Player as p


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.player = p('ISU', 'Iowa State University', 'Cyclones', 'Ames', 'IA', 3, 0, 'Deters', 'River', 5, 'libero')

    def tearDown(self):
        del self.player

    def test_object_created_all_attributes(self):
        self.assertEqual(self.player.school_acronym, 'ISU')
        self.assertEqual(self.player.team_school, 'Iowa State University')
        self.assertEqual(self.player.team_mascot, 'Cyclones')
        self.assertEqual(self.player.team_city, 'Ames')
        self.assertEqual(self.player.team_state, 'IA')
        self.assertEqual(self.player.num_wins, 3)
        self.assertEqual(self.player.num_losses, 0)
        self.assertEqual(self.player.first_name, 'River')
        self.assertEqual(self.player.last_name, 'Deters')
        self.assertEqual(self.player.player_number, 5)
        self.assertEqual(self.player.position, 'libero')

    def test_student_str(self):
        self.assertEqual(str(self.player.__str__()), 'River Deters, player #5, libero.')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(n):
            player = p('ISU', 'Iowa State University', 'Cyclones', 'Ames', 'IA', 3, 0, '$', 'Deters', 5, 'libero')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(n):
            player = p('ISU', 'Iowa State University', 'Cyclones', 'Ames', 'IA', 3, 0, 'River', '$', 5, 'libero')

    def test_object_not_created_error_position(self):
        with self.assertRaises(pos):
            player = p('ISU', 'Iowa State University', 'Cyclones', 'Ames', 'IA', 3, 0, 'River', 'Deters', 5, '$')


if __name__ == '__main__':
    unittest.main()
