# 'Smansoni', 'hookworm', 'ascaris', 'trichuris', 'other_eggs', 'SmansoniPrev', 'HookwormPrev', 'AscarisPrev', 'TrichurisPrev', 'STHPrev'

parasites = ('SmansoniPrev', 'HookwormPrev', 'AscarisPrev', 'TrichurisPrev', 'STHPrev')

for i in parasites:
    print(i)
    odds_ratio(lambda x: x[i] > 0 , lambda x: 2 > x['Q57'] > 3, lambda x: x[i] == 0, lambda x: x['Q57'] < 4, utensils)



def profile_0(df, parasites):
    for i in parasites:
        empty = df[df[i] == 0]
        full = df[df[i] != 0]
        sch_no = len(empty)
        print('{} 0% profile, {} schools'.format(i, sch_no))
        # WASH factors
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15,15))
        plt.suptitle('{} 0% profile, {} schools'.format(i, sch_no))
        ax1.hist(empty['Q1'], bins=3)
        ax1.set_title('water source 1: yes 2: yes, only rainy 3: no')
        ax2.hist(empty['Q29'], bins=7)
        ax2.set_title('type of water source, 1: surface 2:borehole 3: standpipe 4. rainwater 5: protected spring 6: unprotected dug well 7: piped')
        ax3.hist(empty['Q36'], bins=5)
        ax3.set_title('school pay? 1: no, never 2: yes, parents 3: yes, woreda 4: garden income 5: NGOs')
        ax4.hist(empty['Q62'], bins=2)
        ax4.set_title('toilets? 1: yes 2: no')
        plt.savefig(r"C:\dev\data\josh-fyp\outputs\0%Prev\{}_profile.png".format(i))

        fig, (axa, axb, axc, axd) = plt.subplots(4, 1, figsize=(15,15))
        plt.suptitle('{} Non-0% profile, {} schools'.format(i, len(df) - sch_no))
        axa.hist(full['Q1'], bins=3, color='red')
        axa.set_title('water source 1: yes 2: yes, only rainy 3: no')
        axb.hist(full['Q29'], bins=7, color='red')
        axb.set_title('type of water source, 1: surface 2:borehole 3: standpipe 4. rainwater 5: protected spring 6: unprotected dug well 7: piped')
        axc.hist(full['Q36'], bins=5, color='red')
        axc.set_title('school pay? 1: no, never 2: yes, parents 3: yes, woreda 4: garden income 5: NGOs')
        axd.hist(full['Q62'], bins=2, color='red')
        axd.set_title('toilets? 1: yes 2: no')
        plt.savefig(r"C:\dev\data\josh-fyp\outputs\0%Prev\{}_profile_FULL.png".format(i))


# use parasites and sch_kk_climate here
def profile_0_climate(df, parasites):
    for i in parasites:
        empty = df[df[i] == 0]
        full = df[df[i] != 0]
        sch_no = len(empty)
        print('{} 0% profile_climate, {} schools'.format(i, sch_no))
        # Climate factors
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,15))
        plt.suptitle('{} 0% profile_climate, {} schools'.format(i, sch_no))
        ax1.hist(empty['temp_ann'])
        ax1.set_title('TEMP')
        ax1.set_xlim([0, 40])
        ax2.hist(empty['prec_ann'])
        ax2.set_title('PREC')
        ax2.set_xlim([0, 200])
        # plt.savefig(r"C:\dev\data\josh-fyp\outputs\0%Prev\{}_profile.png".format(i))
        plt.show()

        fig, (axa, axb) = plt.subplots(2, 1, figsize=(15,15))
        plt.suptitle('{} Non-0% profile_climate, {} schools'.format(i, len(df) - sch_no))
        axa.hist(full['temp_ann'], color='red')
        axa.set_title('TEMP')
        axa.set_xlim([0, 40])
        axb.hist(full['prec_ann'], color='red')
        axb.set_title('PREC')
        axb.set_xlim([0, 200])
        plt.show()
        # plt.savefig(r"C:\dev\data\josh-fyp\outputs\0%Prev\{}_profile_FULL.png".format(i))