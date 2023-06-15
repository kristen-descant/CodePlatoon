import random

class BoggleBoard:
  all_dice = ['AAEEGN','ELRTTY','AOOTTW','ABBJOO','EHRTVW','CIMOTU',
                 'DISTTY','EIOSST','DELRVY','ACHOPS','HIMNQU','EEINSU',
                 'EEGHNW','AFFKPS','HLNNRZ','DEILRX']
  def __init__(self):
    pass
  def shake(self):
    new_dice_list = self.all_dice[:]
    random.shuffle(new_dice_list)
    new_letter = ""
    for i in range(len(new_dice_list)):
      random_index = random.randint(0,5)
      if i % 4 == 0:
        new_letter += '\n' + new_dice_list[i][random_index]
      else:
        new_letter +=  new_dice_list[i][random_index]
    return new_letter
    # for random.randint(i) in range(len(self.all_dice)):
    #   print()
my_boggle = BoggleBoard()
print(my_boggle.shake())

