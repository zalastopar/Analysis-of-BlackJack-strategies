import pandas as pd

# first key = player, second keys = dealer
decisions = {}
decisions[9] = {2: 'H', 3: 'D', 4: 'D', 5: 'D', 6 : 'D', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[10] = {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'H', 11: 'H'}
decisions[11] = {2: 'D', 3: 'D', 4: 'D', 5: 'D', 6: 'D', 7: 'D', 8: 'D', 9: 'D', 10: 'D', 11: 'D'}
decisions[12] = {2: 'H', 3: 'H', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[13] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[14] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[15] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[16] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
decisions[17] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6: 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}
# pod 9 hit, nad 17 stand

df = pd.DataFrame(decisions)
df.to_csv('data/prob_data_moves.csv')

# ace and smth
# only when player has 2 cards
soft = {}
soft[2] = {2: 'H', 3: 'H', 4: 'H', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[3] = {2: 'H', 3: 'H', 4: 'H', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[4] = {2: 'H', 3: 'H', 4: 'DH', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[5] = {2: 'H', 3: 'H', 4: 'DH', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[6] = {2: 'H', 3: 'DH', 4: 'DH', 5: 'DH', 6 : 'DH', 7: 'H', 8: 'H', 9: 'H', 10: 'H', 11: 'H'}
soft[7] = {2: 'DS', 3: 'DS', 4: 'DS', 5: 'DS', 6 : 'DS', 7: 'S', 8: 'S', 9: 'H', 10: 'H', 11: 'H'}
soft[8] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6 : 'DS', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}
soft[9] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6 : 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}
soft[10] = {2: 'S', 3: 'S', 4: 'S', 5: 'S', 6 : 'S', 7: 'S', 8: 'S', 9: 'S', 10: 'S', 11: 'S'}
df = pd.DataFrame(soft)
df.to_csv('data/soft_data_moves.csv')

# split
splitgrid = {}
splitgrid[2] = {2: 'N', 3: 'N', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[3] = {2: 'N', 3: 'N', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[4] = {2: 'N', 3: 'N', 4: 'N', 5: 'N', 6 : 'N', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[5] = {2: 'N', 3: 'N', 4: 'N', 5: 'N', 6 : 'N', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[6] = {2: 'N', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[7] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[8] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'Y', 9: 'Y', 10: 'Y', 11: 'Y'}
splitgrid[9] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'N', 8: 'Y', 9: 'Y', 10: 'N', 11: 'N'}
splitgrid[10] = {2: 'N', 3: 'N', 4: 'N', 5: 'N', 6 : 'N', 7: 'N', 8: 'N', 9: 'N', 10: 'N', 11: 'N'}
splitgrid[11] = {2: 'Y', 3: 'Y', 4: 'Y', 5: 'Y', 6 : 'Y', 7: 'Y', 8: 'Y', 9: 'Y', 10: 'Y', 11: 'Y'}
df = pd.DataFrame(splitgrid)
df.to_csv('data/split_data_moves.csv')