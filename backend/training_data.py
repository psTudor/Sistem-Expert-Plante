# Set generat automat pentru antrenare
TRAINING_DATA = [
    ("Cum ud orhidee?", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru orhidee?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 53, 'PLANT')]
    }),
    ("Care e expunerea solară ideală pentru orhidee?", {
        "entities": [(38, 45, 'PLANT')]
    }),
    ("Unde ar trebui să așez orhidee pentru lumină optimă?", {
        "entities": [(23, 30, 'PLANT')]
    }),
    ("Ce fel de pământ este recomandat pentru orhidee?", {
        "entities": [(40, 47, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui orhidee?", {
        "entities": [(44, 51, 'PLANT')]
    }),
    ("Informații generale despre orhidee, vă rog.", {
        "entities": [(27, 34, 'PLANT')]
    }),
    ("Cum se îngrijește corect orhidee?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("orhidee are o problemă: frunze galbene.", {
        "entities": [(24, 38, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva frunze galbene la orhidee?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 41, 'PLANT')]
    }),
    ("Am observat frunze galbene la orhidee. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Ce se poate face dacă orhidee suferă de frunze galbene?", {
        "entities": [(40, 54, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("frunze galbene apare des la orhidee? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Este frunze galbene periculoasă pentru orhidee?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 46, 'PLANT')]
    }),
    ("orhidee are o problemă: radacini putrede.", {
        "entities": [(24, 40, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva radacini putrede la orhidee?", {
        "entities": [(16, 32, 'PROBLEM'), (36, 43, 'PLANT')]
    }),
    ("Am observat radacini putrede la orhidee. Ce mă sfătuiți?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Ce se poate face dacă orhidee suferă de radacini putrede?", {
        "entities": [(40, 56, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("radacini putrede apare des la orhidee? Cum tratez?", {
        "entities": [(0, 16, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Este radacini putrede periculoasă pentru orhidee?", {
        "entities": [(5, 21, 'PROBLEM'), (41, 48, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru ficus?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 51, 'PLANT')]
    }),
    ("Cum ud ficus?", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("ficus preferă lumină directă sau difuză?", {
        "entities": [(0, 5, 'PLANT')]
    }),
    ("Ce tip de lumină e ideal pentru ficus?", {
        "entities": [(32, 37, 'PLANT')]
    }),
    ("În ce tip de sol se plantează ficus?", {
        "entities": [(30, 35, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui ficus?", {
        "entities": [(44, 49, 'PLANT')]
    }),
    ("Cum se îngrijește corect ficus?", {
        "entities": [(25, 30, 'PLANT')]
    }),
    ("Cum se cultivă ficus?", {
        "entities": [(15, 20, 'PLANT')]
    }),
    ("ficus are o problemă: cadere frunze.", {
        "entities": [(22, 35, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva cadere frunze la ficus?", {
        "entities": [(16, 29, 'PROBLEM'), (33, 38, 'PLANT')]
    }),
    ("Am observat cadere frunze la ficus. Ce mă sfătuiți?", {
        "entities": [(12, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Ce se poate face dacă ficus suferă de cadere frunze?", {
        "entities": [(38, 51, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("cadere frunze apare des la ficus? Cum tratez?", {
        "entities": [(0, 13, 'PROBLEM'), (27, 32, 'PLANT')]
    }),
    ("Este cadere frunze periculoasă pentru ficus?", {
        "entities": [(5, 18, 'PROBLEM'), (38, 43, 'PLANT')]
    }),
    ("ficus are o problemă: frunze galbene.", {
        "entities": [(22, 36, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva frunze galbene la ficus?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 39, 'PLANT')]
    }),
    ("Am observat frunze galbene la ficus. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Ce se poate face dacă ficus suferă de frunze galbene?", {
        "entities": [(38, 52, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("frunze galbene apare des la ficus? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 33, 'PLANT')]
    }),
    ("Este frunze galbene periculoasă pentru ficus?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 44, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru trandafir?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 48, 'PLANT')]
    }),
    ("Cum ud trandafir?", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("trandafir preferă lumină directă sau difuză?", {
        "entities": [(0, 9, 'PLANT')]
    }),
    ("Câtă lumină are nevoie trandafir pe zi?", {
        "entities": [(23, 32, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui trandafir?", {
        "entities": [(44, 53, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine trandafir?", {
        "entities": [(39, 48, 'PLANT')]
    }),
    ("Cum se cultivă trandafir?", {
        "entities": [(15, 24, 'PLANT')]
    }),
    ("Ce condiții sunt ideale pentru trandafir?", {
        "entities": [(31, 40, 'PLANT')]
    }),
    ("trandafir are o problemă: frunze galbene.", {
        "entities": [(26, 40, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum pot rezolva frunze galbene la trandafir?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 43, 'PLANT')]
    }),
    ("Am observat frunze galbene la trandafir. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("Ce se poate face dacă trandafir suferă de frunze galbene?", {
        "entities": [(42, 56, 'PROBLEM'), (22, 31, 'PLANT')]
    }),
    ("frunze galbene apare des la trandafir? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 37, 'PLANT')]
    }),
    ("Este frunze galbene periculoasă pentru trandafir?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 48, 'PLANT')]
    }),
    ("trandafir are o problemă: pete negre.", {
        "entities": [(26, 36, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum pot rezolva pete negre la trandafir?", {
        "entities": [(16, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("Am observat pete negre la trandafir. Ce mă sfătuiți?", {
        "entities": [(12, 22, 'PROBLEM'), (26, 35, 'PLANT')]
    }),
    ("Ce se poate face dacă trandafir suferă de pete negre?", {
        "entities": [(42, 52, 'PROBLEM'), (22, 31, 'PLANT')]
    }),
    ("pete negre apare des la trandafir? Cum tratez?", {
        "entities": [(0, 10, 'PROBLEM'), (24, 33, 'PLANT')]
    }),
    ("Este pete negre periculoasă pentru trandafir?", {
        "entities": [(5, 15, 'PROBLEM'), (35, 44, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru crin?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 50, 'PLANT')]
    }),
    ("Cât de des trebuie udată crin?", {
        "entities": [(25, 29, 'PLANT')]
    }),
    ("Ce fel de lumină preferă crin?", {
        "entities": [(25, 29, 'PLANT')]
    }),
    ("Câtă lumină are nevoie crin pe zi?", {
        "entities": [(23, 27, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine crin?", {
        "entities": [(39, 43, 'PLANT')]
    }),
    ("Ce compoziție de sol preferă crin?", {
        "entities": [(29, 33, 'PLANT')]
    }),
    ("Aveți sfaturi pentru creșterea lui crin?", {
        "entities": [(35, 39, 'PLANT')]
    }),
    ("Informații generale despre crin, vă rog.", {
        "entities": [(27, 31, 'PLANT')]
    }),
    ("crin are o problemă: ingalbenirea frunzelor.", {
        "entities": [(21, 43, 'PROBLEM'), (0, 4, 'PLANT')]
    }),
    ("Cum pot rezolva ingalbenirea frunzelor la crin?", {
        "entities": [(16, 38, 'PROBLEM'), (42, 46, 'PLANT')]
    }),
    ("Am observat ingalbenirea frunzelor la crin. Ce mă sfătuiți?", {
        "entities": [(12, 34, 'PROBLEM'), (38, 42, 'PLANT')]
    }),
    ("Ce se poate face dacă crin suferă de ingalbenirea frunzelor?", {
        "entities": [(37, 59, 'PROBLEM'), (22, 26, 'PLANT')]
    }),
    ("ingalbenirea frunzelor apare des la crin? Cum tratez?", {
        "entities": [(0, 22, 'PROBLEM'), (36, 40, 'PLANT')]
    }),
    ("Este ingalbenirea frunzelor periculoasă pentru crin?", {
        "entities": [(5, 27, 'PROBLEM'), (47, 51, 'PLANT')]
    }),
    ("crin are o problemă: lipsa inflorire.", {
        "entities": [(21, 36, 'PROBLEM'), (0, 4, 'PLANT')]
    }),
    ("Cum pot rezolva lipsa inflorire la crin?", {
        "entities": [(16, 31, 'PROBLEM'), (35, 39, 'PLANT')]
    }),
    ("Am observat lipsa inflorire la crin. Ce mă sfătuiți?", {
        "entities": [(12, 27, 'PROBLEM'), (31, 35, 'PLANT')]
    }),
    ("Ce se poate face dacă crin suferă de lipsa inflorire?", {
        "entities": [(37, 52, 'PROBLEM'), (22, 26, 'PLANT')]
    }),
    ("lipsa inflorire apare des la crin? Cum tratez?", {
        "entities": [(0, 15, 'PROBLEM'), (29, 33, 'PLANT')]
    }),
    ("Este lipsa inflorire periculoasă pentru crin?", {
        "entities": [(5, 20, 'PROBLEM'), (40, 44, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru muscata?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 46, 'PLANT')]
    }),
    ("Cât de des trebuie udată muscata?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Ce fel de lumină preferă muscata?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Care e expunerea solară ideală pentru muscata?", {
        "entities": [(38, 45, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine muscata?", {
        "entities": [(39, 46, 'PLANT')]
    }),
    ("În ce tip de sol se plantează muscata?", {
        "entities": [(30, 37, 'PLANT')]
    }),
    ("Care sunt cerințele de bază ale plantei muscata?", {
        "entities": [(40, 47, 'PLANT')]
    }),
    ("Cum mențin sănătoasă planta muscata?", {
        "entities": [(28, 35, 'PLANT')]
    }),
    ("muscata are o problemă: frunze galbene.", {
        "entities": [(24, 38, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva frunze galbene la muscata?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 41, 'PLANT')]
    }),
    ("Am observat frunze galbene la muscata. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Ce se poate face dacă muscata suferă de frunze galbene?", {
        "entities": [(40, 54, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("frunze galbene apare des la muscata? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Este frunze galbene periculoasă pentru muscata?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 46, 'PLANT')]
    }),
    ("muscata are o problemă: putine flori.", {
        "entities": [(24, 36, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva putine flori la muscata?", {
        "entities": [(16, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Am observat putine flori la muscata. Ce mă sfătuiți?", {
        "entities": [(12, 24, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Ce se poate face dacă muscata suferă de putine flori?", {
        "entities": [(40, 52, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("putine flori apare des la muscata? Cum tratez?", {
        "entities": [(0, 12, 'PROBLEM'), (26, 33, 'PLANT')]
    }),
    ("Este putine flori periculoasă pentru muscata?", {
        "entities": [(5, 17, 'PROBLEM'), (37, 44, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru aloe vera?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 55, 'PLANT')]
    }),
    ("Cât de des trebuie udată aloe vera?", {
        "entities": [(25, 34, 'PLANT')]
    }),
    ("Ce fel de lumină preferă aloe vera?", {
        "entities": [(25, 34, 'PLANT')]
    }),
    ("Ce tip de lumină e ideal pentru aloe vera?", {
        "entities": [(32, 41, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui aloe vera?", {
        "entities": [(44, 53, 'PLANT')]
    }),
    ("În ce tip de sol se plantează aloe vera?", {
        "entities": [(30, 39, 'PLANT')]
    }),
    ("Cum pot avea grijă eficient de aloe vera?", {
        "entities": [(31, 40, 'PLANT')]
    }),
    ("Cum se îngrijește corect aloe vera?", {
        "entities": [(25, 34, 'PLANT')]
    }),
    ("aloe vera are o problemă: frunze maro.", {
        "entities": [(26, 37, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum pot rezolva frunze maro la aloe vera?", {
        "entities": [(16, 27, 'PROBLEM'), (31, 40, 'PLANT')]
    }),
    ("Am observat frunze maro la aloe vera. Ce mă sfătuiți?", {
        "entities": [(12, 23, 'PROBLEM'), (27, 36, 'PLANT')]
    }),
    ("Ce se poate face dacă aloe vera suferă de frunze maro?", {
        "entities": [(42, 53, 'PROBLEM'), (22, 31, 'PLANT')]
    }),
    ("frunze maro apare des la aloe vera? Cum tratez?", {
        "entities": [(0, 11, 'PROBLEM'), (25, 34, 'PLANT')]
    }),
    ("Este frunze maro periculoasă pentru aloe vera?", {
        "entities": [(5, 16, 'PROBLEM'), (36, 45, 'PLANT')]
    }),
    ("aloe vera are o problemă: frunze moi.", {
        "entities": [(26, 36, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum pot rezolva frunze moi la aloe vera?", {
        "entities": [(16, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("Am observat frunze moi la aloe vera. Ce mă sfătuiți?", {
        "entities": [(12, 22, 'PROBLEM'), (26, 35, 'PLANT')]
    }),
    ("Ce se poate face dacă aloe vera suferă de frunze moi?", {
        "entities": [(42, 52, 'PROBLEM'), (22, 31, 'PLANT')]
    }),
    ("frunze moi apare des la aloe vera? Cum tratez?", {
        "entities": [(0, 10, 'PROBLEM'), (24, 33, 'PLANT')]
    }),
    ("Este frunze moi periculoasă pentru aloe vera?", {
        "entities": [(5, 15, 'PROBLEM'), (35, 44, 'PLANT')]
    }),
    ("aloe vera are o problemă: putrezirea bazei.", {
        "entities": [(26, 42, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum pot rezolva putrezirea bazei la aloe vera?", {
        "entities": [(16, 32, 'PROBLEM'), (36, 45, 'PLANT')]
    }),
    ("Am observat putrezirea bazei la aloe vera. Ce mă sfătuiți?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 41, 'PLANT')]
    }),
    ("Ce se poate face dacă aloe vera suferă de putrezirea bazei?", {
        "entities": [(42, 58, 'PROBLEM'), (22, 31, 'PLANT')]
    }),
    ("putrezirea bazei apare des la aloe vera? Cum tratez?", {
        "entities": [(0, 16, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("Este putrezirea bazei periculoasă pentru aloe vera?", {
        "entities": [(5, 21, 'PROBLEM'), (41, 50, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru cactus?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 52, 'PLANT')]
    }),
    ("Cât de des trebuie udată cactus?", {
        "entities": [(25, 31, 'PLANT')]
    }),
    ("Care e expunerea solară ideală pentru cactus?", {
        "entities": [(38, 44, 'PLANT')]
    }),
    ("cactus preferă lumină directă sau difuză?", {
        "entities": [(0, 6, 'PLANT')]
    }),
    ("Ce compoziție de sol preferă cactus?", {
        "entities": [(29, 35, 'PLANT')]
    }),
    ("Ce fel de pământ este recomandat pentru cactus?", {
        "entities": [(40, 46, 'PLANT')]
    }),
    ("Cum se îngrijește corect cactus?", {
        "entities": [(25, 31, 'PLANT')]
    }),
    ("Ce trebuie să știu despre cactus?", {
        "entities": [(26, 32, 'PLANT')]
    }),
    ("cactus are o problemă: putrezire baza.", {
        "entities": [(23, 37, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum pot rezolva putrezire baza la cactus?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 40, 'PLANT')]
    }),
    ("Am observat putrezire baza la cactus. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 36, 'PLANT')]
    }),
    ("Ce se poate face dacă cactus suferă de putrezire baza?", {
        "entities": [(39, 53, 'PROBLEM'), (22, 28, 'PLANT')]
    }),
    ("putrezire baza apare des la cactus? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 34, 'PLANT')]
    }),
    ("Este putrezire baza periculoasă pentru cactus?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 45, 'PLANT')]
    }),
    ("cactus are o problemă: crestere alungita.", {
        "entities": [(23, 40, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum pot rezolva crestere alungita la cactus?", {
        "entities": [(16, 33, 'PROBLEM'), (37, 43, 'PLANT')]
    }),
    ("Am observat crestere alungita la cactus. Ce mă sfătuiți?", {
        "entities": [(12, 29, 'PROBLEM'), (33, 39, 'PLANT')]
    }),
    ("Ce se poate face dacă cactus suferă de crestere alungita?", {
        "entities": [(39, 56, 'PROBLEM'), (22, 28, 'PLANT')]
    }),
    ("crestere alungita apare des la cactus? Cum tratez?", {
        "entities": [(0, 17, 'PROBLEM'), (31, 37, 'PLANT')]
    }),
    ("Este crestere alungita periculoasă pentru cactus?", {
        "entities": [(5, 22, 'PROBLEM'), (42, 48, 'PLANT')]
    }),
    ("cactus are o problemă: pete maronii.", {
        "entities": [(23, 35, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum pot rezolva pete maronii la cactus?", {
        "entities": [(16, 28, 'PROBLEM'), (32, 38, 'PLANT')]
    }),
    ("Am observat pete maronii la cactus. Ce mă sfătuiți?", {
        "entities": [(12, 24, 'PROBLEM'), (28, 34, 'PLANT')]
    }),
    ("Ce se poate face dacă cactus suferă de pete maronii?", {
        "entities": [(39, 51, 'PROBLEM'), (22, 28, 'PLANT')]
    }),
    ("pete maronii apare des la cactus? Cum tratez?", {
        "entities": [(0, 12, 'PROBLEM'), (26, 32, 'PLANT')]
    }),
    ("Este pete maronii periculoasă pentru cactus?", {
        "entities": [(5, 17, 'PROBLEM'), (37, 43, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru lavanda?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 46, 'PLANT')]
    }),
    ("Cât de des trebuie udată lavanda?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Ce fel de lumină preferă lavanda?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Câtă lumină are nevoie lavanda pe zi?", {
        "entities": [(23, 30, 'PLANT')]
    }),
    ("În ce tip de sol se plantează lavanda?", {
        "entities": [(30, 37, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine lavanda?", {
        "entities": [(39, 46, 'PLANT')]
    }),
    ("Aveți sfaturi pentru creșterea lui lavanda?", {
        "entities": [(35, 42, 'PLANT')]
    }),
    ("Ce condiții sunt ideale pentru lavanda?", {
        "entities": [(31, 38, 'PLANT')]
    }),
    ("lavanda are o problemă: radacini putrede.", {
        "entities": [(24, 40, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva radacini putrede la lavanda?", {
        "entities": [(16, 32, 'PROBLEM'), (36, 43, 'PLANT')]
    }),
    ("Am observat radacini putrede la lavanda. Ce mă sfătuiți?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Ce se poate face dacă lavanda suferă de radacini putrede?", {
        "entities": [(40, 56, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("radacini putrede apare des la lavanda? Cum tratez?", {
        "entities": [(0, 16, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Este radacini putrede periculoasă pentru lavanda?", {
        "entities": [(5, 21, 'PROBLEM'), (41, 48, 'PLANT')]
    }),
    ("lavanda are o problemă: crestere lemnoasa.", {
        "entities": [(24, 41, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva crestere lemnoasa la lavanda?", {
        "entities": [(16, 33, 'PROBLEM'), (37, 44, 'PLANT')]
    }),
    ("Am observat crestere lemnoasa la lavanda. Ce mă sfătuiți?", {
        "entities": [(12, 29, 'PROBLEM'), (33, 40, 'PLANT')]
    }),
    ("Ce se poate face dacă lavanda suferă de crestere lemnoasa?", {
        "entities": [(40, 57, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("crestere lemnoasa apare des la lavanda? Cum tratez?", {
        "entities": [(0, 17, 'PROBLEM'), (31, 38, 'PLANT')]
    }),
    ("Este crestere lemnoasa periculoasă pentru lavanda?", {
        "entities": [(5, 22, 'PROBLEM'), (42, 49, 'PLANT')]
    }),
    ("lavanda are o problemă: frunze galbene.", {
        "entities": [(24, 38, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva frunze galbene la lavanda?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 41, 'PLANT')]
    }),
    ("Am observat frunze galbene la lavanda. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Ce se poate face dacă lavanda suferă de frunze galbene?", {
        "entities": [(40, 54, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("frunze galbene apare des la lavanda? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Este frunze galbene periculoasă pentru lavanda?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 46, 'PLANT')]
    }),
    ("Cât de des trebuie udată lalea?", {
        "entities": [(25, 30, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru lalea?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 44, 'PLANT')]
    }),
    ("Unde ar trebui să așez lalea pentru lumină optimă?", {
        "entities": [(23, 28, 'PLANT')]
    }),
    ("Care e expunerea solară ideală pentru lalea?", {
        "entities": [(38, 43, 'PLANT')]
    }),
    ("Ce fel de pământ este recomandat pentru lalea?", {
        "entities": [(40, 45, 'PLANT')]
    }),
    ("Ce compoziție de sol preferă lalea?", {
        "entities": [(29, 34, 'PLANT')]
    }),
    ("Cum se îngrijește corect lalea?", {
        "entities": [(25, 30, 'PLANT')]
    }),
    ("Informații generale despre lalea, vă rog.", {
        "entities": [(27, 32, 'PLANT')]
    }),
    ("lalea are o problemă: lipsa inflorire.", {
        "entities": [(22, 37, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva lipsa inflorire la lalea?", {
        "entities": [(16, 31, 'PROBLEM'), (35, 40, 'PLANT')]
    }),
    ("Am observat lipsa inflorire la lalea. Ce mă sfătuiți?", {
        "entities": [(12, 27, 'PROBLEM'), (31, 36, 'PLANT')]
    }),
    ("Ce se poate face dacă lalea suferă de lipsa inflorire?", {
        "entities": [(38, 53, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("lipsa inflorire apare des la lalea? Cum tratez?", {
        "entities": [(0, 15, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Este lipsa inflorire periculoasă pentru lalea?", {
        "entities": [(5, 20, 'PROBLEM'), (40, 45, 'PLANT')]
    }),
    ("lalea are o problemă: tulpini scurte.", {
        "entities": [(22, 36, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva tulpini scurte la lalea?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 39, 'PLANT')]
    }),
    ("Am observat tulpini scurte la lalea. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Ce se poate face dacă lalea suferă de tulpini scurte?", {
        "entities": [(38, 52, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("tulpini scurte apare des la lalea? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 33, 'PLANT')]
    }),
    ("Este tulpini scurte periculoasă pentru lalea?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 44, 'PLANT')]
    }),
    ("lalea are o problemă: putrezirea bulbilor.", {
        "entities": [(22, 41, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva putrezirea bulbilor la lalea?", {
        "entities": [(16, 35, 'PROBLEM'), (39, 44, 'PLANT')]
    }),
    ("Am observat putrezirea bulbilor la lalea. Ce mă sfătuiți?", {
        "entities": [(12, 31, 'PROBLEM'), (35, 40, 'PLANT')]
    }),
    ("Ce se poate face dacă lalea suferă de putrezirea bulbilor?", {
        "entities": [(38, 57, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("putrezirea bulbilor apare des la lalea? Cum tratez?", {
        "entities": [(0, 19, 'PROBLEM'), (33, 38, 'PLANT')]
    }),
    ("Este putrezirea bulbilor periculoasă pentru lalea?", {
        "entities": [(5, 24, 'PROBLEM'), (44, 49, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru bujor?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 51, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru bujor?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 44, 'PLANT')]
    }),
    ("Câtă lumină are nevoie bujor pe zi?", {
        "entities": [(23, 28, 'PLANT')]
    }),
    ("Ce tip de lumină e ideal pentru bujor?", {
        "entities": [(32, 37, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine bujor?", {
        "entities": [(39, 44, 'PLANT')]
    }),
    ("Ce compoziție de sol preferă bujor?", {
        "entities": [(29, 34, 'PLANT')]
    }),
    ("Cum mențin sănătoasă planta bujor?", {
        "entities": [(28, 33, 'PLANT')]
    }),
    ("Cum se cultivă bujor?", {
        "entities": [(15, 20, 'PLANT')]
    }),
    ("bujor are o problemă: lipsa inflorire.", {
        "entities": [(22, 37, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva lipsa inflorire la bujor?", {
        "entities": [(16, 31, 'PROBLEM'), (35, 40, 'PLANT')]
    }),
    ("Am observat lipsa inflorire la bujor. Ce mă sfătuiți?", {
        "entities": [(12, 27, 'PROBLEM'), (31, 36, 'PLANT')]
    }),
    ("Ce se poate face dacă bujor suferă de lipsa inflorire?", {
        "entities": [(38, 53, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("lipsa inflorire apare des la bujor? Cum tratez?", {
        "entities": [(0, 15, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Este lipsa inflorire periculoasă pentru bujor?", {
        "entities": [(5, 20, 'PROBLEM'), (40, 45, 'PLANT')]
    }),
    ("bujor are o problemă: frunze patate.", {
        "entities": [(22, 35, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva frunze patate la bujor?", {
        "entities": [(16, 29, 'PROBLEM'), (33, 38, 'PLANT')]
    }),
    ("Am observat frunze patate la bujor. Ce mă sfătuiți?", {
        "entities": [(12, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Ce se poate face dacă bujor suferă de frunze patate?", {
        "entities": [(38, 51, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("frunze patate apare des la bujor? Cum tratez?", {
        "entities": [(0, 13, 'PROBLEM'), (27, 32, 'PLANT')]
    }),
    ("Este frunze patate periculoasă pentru bujor?", {
        "entities": [(5, 18, 'PROBLEM'), (38, 43, 'PLANT')]
    }),
    ("bujor are o problemă: boboci care nu se deschid.", {
        "entities": [(22, 47, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum pot rezolva boboci care nu se deschid la bujor?", {
        "entities": [(16, 41, 'PROBLEM'), (45, 50, 'PLANT')]
    }),
    ("Am observat boboci care nu se deschid la bujor. Ce mă sfătuiți?", {
        "entities": [(12, 37, 'PROBLEM'), (41, 46, 'PLANT')]
    }),
    ("Ce se poate face dacă bujor suferă de boboci care nu se deschid?", {
        "entities": [(38, 63, 'PROBLEM'), (22, 27, 'PLANT')]
    }),
    ("boboci care nu se deschid apare des la bujor? Cum tratez?", {
        "entities": [(0, 25, 'PROBLEM'), (39, 44, 'PLANT')]
    }),
    ("Este boboci care nu se deschid periculoasă pentru bujor?", {
        "entities": [(5, 30, 'PROBLEM'), (50, 55, 'PLANT')]
    }),
    ("Cât de des trebuie udată magnolie?", {
        "entities": [(25, 33, 'PLANT')]
    }),
    ("Cum ud magnolie?", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Câtă lumină are nevoie magnolie pe zi?", {
        "entities": [(23, 31, 'PLANT')]
    }),
    ("Ce fel de lumină preferă magnolie?", {
        "entities": [(25, 33, 'PLANT')]
    }),
    ("Ce compoziție de sol preferă magnolie?", {
        "entities": [(29, 37, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine magnolie?", {
        "entities": [(39, 47, 'PLANT')]
    }),
    ("Aveți sfaturi pentru creșterea lui magnolie?", {
        "entities": [(35, 43, 'PLANT')]
    }),
    ("Cum se îngrijește corect magnolie?", {
        "entities": [(25, 33, 'PLANT')]
    }),
    ("magnolie are o problemă: inghet flori.", {
        "entities": [(25, 37, 'PROBLEM'), (0, 8, 'PLANT')]
    }),
    ("Cum pot rezolva inghet flori la magnolie?", {
        "entities": [(16, 28, 'PROBLEM'), (32, 40, 'PLANT')]
    }),
    ("Am observat inghet flori la magnolie. Ce mă sfătuiți?", {
        "entities": [(12, 24, 'PROBLEM'), (28, 36, 'PLANT')]
    }),
    ("Ce se poate face dacă magnolie suferă de inghet flori?", {
        "entities": [(41, 53, 'PROBLEM'), (22, 30, 'PLANT')]
    }),
    ("inghet flori apare des la magnolie? Cum tratez?", {
        "entities": [(0, 12, 'PROBLEM'), (26, 34, 'PLANT')]
    }),
    ("Este inghet flori periculoasă pentru magnolie?", {
        "entities": [(5, 17, 'PROBLEM'), (37, 45, 'PLANT')]
    }),
    ("magnolie are o problemă: frunze galbene.", {
        "entities": [(25, 39, 'PROBLEM'), (0, 8, 'PLANT')]
    }),
    ("Cum pot rezolva frunze galbene la magnolie?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 42, 'PLANT')]
    }),
    ("Am observat frunze galbene la magnolie. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("Ce se poate face dacă magnolie suferă de frunze galbene?", {
        "entities": [(41, 55, 'PROBLEM'), (22, 30, 'PLANT')]
    }),
    ("frunze galbene apare des la magnolie? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 36, 'PLANT')]
    }),
    ("Este frunze galbene periculoasă pentru magnolie?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 47, 'PLANT')]
    }),
    ("magnolie are o problemă: scoarta deteriorata.", {
        "entities": [(25, 44, 'PROBLEM'), (0, 8, 'PLANT')]
    }),
    ("Cum pot rezolva scoarta deteriorata la magnolie?", {
        "entities": [(16, 35, 'PROBLEM'), (39, 47, 'PLANT')]
    }),
    ("Am observat scoarta deteriorata la magnolie. Ce mă sfătuiți?", {
        "entities": [(12, 31, 'PROBLEM'), (35, 43, 'PLANT')]
    }),
    ("Ce se poate face dacă magnolie suferă de scoarta deteriorata?", {
        "entities": [(41, 60, 'PROBLEM'), (22, 30, 'PLANT')]
    }),
    ("scoarta deteriorata apare des la magnolie? Cum tratez?", {
        "entities": [(0, 19, 'PROBLEM'), (33, 41, 'PLANT')]
    }),
    ("Este scoarta deteriorata periculoasă pentru magnolie?", {
        "entities": [(5, 24, 'PROBLEM'), (44, 52, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru liliac?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 45, 'PLANT')]
    }),
    ("Cât de des trebuie udată liliac?", {
        "entities": [(25, 31, 'PLANT')]
    }),
    ("Câtă lumină are nevoie liliac pe zi?", {
        "entities": [(23, 29, 'PLANT')]
    }),
    ("Ce tip de lumină e ideal pentru liliac?", {
        "entities": [(32, 38, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine liliac?", {
        "entities": [(39, 45, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui liliac?", {
        "entities": [(44, 50, 'PLANT')]
    }),
    ("Informații generale despre liliac, vă rog.", {
        "entities": [(27, 33, 'PLANT')]
    }),
    ("Aveți sfaturi pentru creșterea lui liliac?", {
        "entities": [(35, 41, 'PLANT')]
    }),
    ("liliac are o problemă: lipsa florilor.", {
        "entities": [(23, 37, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum pot rezolva lipsa florilor la liliac?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 40, 'PLANT')]
    }),
    ("Am observat lipsa florilor la liliac. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 36, 'PLANT')]
    }),
    ("Ce se poate face dacă liliac suferă de lipsa florilor?", {
        "entities": [(39, 53, 'PROBLEM'), (22, 28, 'PLANT')]
    }),
    ("lipsa florilor apare des la liliac? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 34, 'PLANT')]
    }),
    ("Este lipsa florilor periculoasă pentru liliac?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 45, 'PLANT')]
    }),
    ("liliac are o problemă: pete pe frunze.", {
        "entities": [(23, 37, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum pot rezolva pete pe frunze la liliac?", {
        "entities": [(16, 30, 'PROBLEM'), (34, 40, 'PLANT')]
    }),
    ("Am observat pete pe frunze la liliac. Ce mă sfătuiți?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 36, 'PLANT')]
    }),
    ("Ce se poate face dacă liliac suferă de pete pe frunze?", {
        "entities": [(39, 53, 'PROBLEM'), (22, 28, 'PLANT')]
    }),
    ("pete pe frunze apare des la liliac? Cum tratez?", {
        "entities": [(0, 14, 'PROBLEM'), (28, 34, 'PLANT')]
    }),
    ("Este pete pe frunze periculoasă pentru liliac?", {
        "entities": [(5, 19, 'PROBLEM'), (39, 45, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru iris?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 43, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru iris?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 50, 'PLANT')]
    }),
    ("Care e expunerea solară ideală pentru iris?", {
        "entities": [(38, 42, 'PLANT')]
    }),
    ("iris preferă lumină directă sau difuză?", {
        "entities": [(0, 4, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui iris?", {
        "entities": [(44, 48, 'PLANT')]
    }),
    ("Ce compoziție de sol preferă iris?", {
        "entities": [(29, 33, 'PLANT')]
    }),
    ("Cum pot avea grijă eficient de iris?", {
        "entities": [(31, 35, 'PLANT')]
    }),
    ("Cum mențin sănătoasă planta iris?", {
        "entities": [(28, 32, 'PLANT')]
    }),
    ("iris are o problemă: putrezirea rizomului.", {
        "entities": [(21, 41, 'PROBLEM'), (0, 4, 'PLANT')]
    }),
    ("Cum pot rezolva putrezirea rizomului la iris?", {
        "entities": [(16, 36, 'PROBLEM'), (40, 44, 'PLANT')]
    }),
    ("Am observat putrezirea rizomului la iris. Ce mă sfătuiți?", {
        "entities": [(12, 32, 'PROBLEM'), (36, 40, 'PLANT')]
    }),
    ("Ce se poate face dacă iris suferă de putrezirea rizomului?", {
        "entities": [(37, 57, 'PROBLEM'), (22, 26, 'PLANT')]
    }),
    ("putrezirea rizomului apare des la iris? Cum tratez?", {
        "entities": [(0, 20, 'PROBLEM'), (34, 38, 'PLANT')]
    }),
    ("Este putrezirea rizomului periculoasă pentru iris?", {
        "entities": [(5, 25, 'PROBLEM'), (45, 49, 'PLANT')]
    }),
    ("Cât de des trebuie udată garoafa?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru garoafa?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 46, 'PLANT')]
    }),
    ("Câtă lumină are nevoie garoafa pe zi?", {
        "entities": [(23, 30, 'PLANT')]
    }),
    ("garoafa preferă lumină directă sau difuză?", {
        "entities": [(0, 7, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine garoafa?", {
        "entities": [(39, 46, 'PLANT')]
    }),
    ("În ce tip de sol se plantează garoafa?", {
        "entities": [(30, 37, 'PLANT')]
    }),
    ("Ce trebuie să știu despre garoafa?", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Cum se îngrijește corect garoafa?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("garoafa are o problemă: ofilirea florilor.", {
        "entities": [(24, 41, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum pot rezolva ofilirea florilor la garoafa?", {
        "entities": [(16, 33, 'PROBLEM'), (37, 44, 'PLANT')]
    }),
    ("Am observat ofilirea florilor la garoafa. Ce mă sfătuiți?", {
        "entities": [(12, 29, 'PROBLEM'), (33, 40, 'PLANT')]
    }),
    ("Ce se poate face dacă garoafa suferă de ofilirea florilor?", {
        "entities": [(40, 57, 'PROBLEM'), (22, 29, 'PLANT')]
    }),
    ("ofilirea florilor apare des la garoafa? Cum tratez?", {
        "entities": [(0, 17, 'PROBLEM'), (31, 38, 'PLANT')]
    }),
    ("Este ofilirea florilor periculoasă pentru garoafa?", {
        "entities": [(5, 22, 'PROBLEM'), (42, 49, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru tuia?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 43, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru tuia?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 50, 'PLANT')]
    }),
    ("Care e expunerea solară ideală pentru tuia?", {
        "entities": [(38, 42, 'PLANT')]
    }),
    ("Ce tip de lumină e ideal pentru tuia?", {
        "entities": [(32, 36, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui tuia?", {
        "entities": [(44, 48, 'PLANT')]
    }),
    ("În ce tip de sol se plantează tuia?", {
        "entities": [(30, 34, 'PLANT')]
    }),
    ("Cum pot avea grijă eficient de tuia?", {
        "entities": [(31, 35, 'PLANT')]
    }),
    ("Cum mențin sănătoasă planta tuia?", {
        "entities": [(28, 32, 'PLANT')]
    }),
    ("tuia are o problemă: brunificare varfuri.", {
        "entities": [(21, 40, 'PROBLEM'), (0, 4, 'PLANT')]
    }),
    ("Cum pot rezolva brunificare varfuri la tuia?", {
        "entities": [(16, 35, 'PROBLEM'), (39, 43, 'PLANT')]
    }),
    ("Am observat brunificare varfuri la tuia. Ce mă sfătuiți?", {
        "entities": [(12, 31, 'PROBLEM'), (35, 39, 'PLANT')]
    }),
    ("Ce se poate face dacă tuia suferă de brunificare varfuri?", {
        "entities": [(37, 56, 'PROBLEM'), (22, 26, 'PLANT')]
    }),
    ("brunificare varfuri apare des la tuia? Cum tratez?", {
        "entities": [(0, 19, 'PROBLEM'), (33, 37, 'PLANT')]
    }),
    ("Este brunificare varfuri periculoasă pentru tuia?", {
        "entities": [(5, 24, 'PROBLEM'), (44, 48, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru bonsai?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 52, 'PLANT')]
    }),
    ("La ce interval se udă bonsai?", {
        "entities": [(22, 28, 'PLANT')]
    }),
    ("bonsai preferă lumină directă sau difuză?", {
        "entities": [(0, 6, 'PLANT')]
    }),
    ("Unde ar trebui să așez bonsai pentru lumină optimă?", {
        "entities": [(23, 29, 'PLANT')]
    }),
    ("Care e mediul potrivit pentru plantarea lui bonsai?", {
        "entities": [(44, 50, 'PLANT')]
    }),
    ("În ce tip de sol se plantează bonsai?", {
        "entities": [(30, 36, 'PLANT')]
    }),
    ("Cum se îngrijește corect bonsai?", {
        "entities": [(25, 31, 'PLANT')]
    }),
    ("Aveți sfaturi pentru creșterea lui bonsai?", {
        "entities": [(35, 41, 'PLANT')]
    }),
    ("bonsai are o problemă: frunze cazatoare.", {
        "entities": [(23, 39, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum pot rezolva frunze cazatoare la bonsai?", {
        "entities": [(16, 32, 'PROBLEM'), (36, 42, 'PLANT')]
    }),
    ("Am observat frunze cazatoare la bonsai. Ce mă sfătuiți?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 38, 'PLANT')]
    }),
    ("Ce se poate face dacă bonsai suferă de frunze cazatoare?", {
        "entities": [(39, 55, 'PROBLEM'), (22, 28, 'PLANT')]
    }),
    ("frunze cazatoare apare des la bonsai? Cum tratez?", {
        "entities": [(0, 16, 'PROBLEM'), (30, 36, 'PLANT')]
    }),
    ("Este frunze cazatoare periculoasă pentru bonsai?", {
        "entities": [(5, 21, 'PROBLEM'), (41, 47, 'PLANT')]
    }),
    ("Cât de des trebuie udată crizantema?", {
        "entities": [(25, 35, 'PLANT')]
    }),
    ("Cum ud crizantema?", {
        "entities": [(7, 17, 'PLANT')]
    }),
    ("Unde ar trebui să așez crizantema pentru lumină optimă?", {
        "entities": [(23, 33, 'PLANT')]
    }),
    ("Ce tip de lumină e ideal pentru crizantema?", {
        "entities": [(32, 42, 'PLANT')]
    }),
    ("Ce fel de pământ este recomandat pentru crizantema?", {
        "entities": [(40, 50, 'PLANT')]
    }),
    ("Cu ce fel de pământ merge cel mai bine crizantema?", {
        "entities": [(39, 49, 'PLANT')]
    }),
    ("Ce trebuie să știu despre crizantema?", {
        "entities": [(26, 36, 'PLANT')]
    }),
    ("Aveți sfaturi pentru creșterea lui crizantema?", {
        "entities": [(35, 45, 'PLANT')]
    }),
    ("crizantema are o problemă: mucegai pe frunze.", {
        "entities": [(27, 44, 'PROBLEM'), (0, 10, 'PLANT')]
    }),
    ("Cum pot rezolva mucegai pe frunze la crizantema?", {
        "entities": [(16, 33, 'PROBLEM'), (37, 47, 'PLANT')]
    }),
    ("Am observat mucegai pe frunze la crizantema. Ce mă sfătuiți?", {
        "entities": [(12, 29, 'PROBLEM'), (33, 43, 'PLANT')]
    }),
    ("Ce se poate face dacă crizantema suferă de mucegai pe frunze?", {
        "entities": [(43, 60, 'PROBLEM'), (22, 32, 'PLANT')]
    }),
    ("mucegai pe frunze apare des la crizantema? Cum tratez?", {
        "entities": [(0, 17, 'PROBLEM'), (31, 41, 'PLANT')]
    }),
    ("Este mucegai pe frunze periculoasă pentru crizantema?", {
        "entities": [(5, 22, 'PROBLEM'), (42, 52, 'PLANT')]
    }),
    ("Care este frecvența de udare potrivită pentru craciunita?", {
        "entities": [(23, 28, 'CARE_ASPECT'), (46, 56, 'PLANT')]
    }),
    ("Ce metodă de udare se folosește pentru craciunita?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (39, 49, 'PLANT')]
    }),
    ("craciunita preferă lumină directă sau difuză?", {
        "entities": [(0, 10, 'PLANT')]
    }),
    ("Ce fel de lumină preferă craciunita?", {
        "entities": [(25, 35, 'PLANT')]
    }),
    ("Ce compoziție de sol preferă craciunita?", {
        "entities": [(29, 39, 'PLANT')]
    }),
    ("Ce fel de pământ este recomandat pentru craciunita?", {
        "entities": [(40, 50, 'PLANT')]
    }),
    ("Informații generale despre craciunita, vă rog.", {
        "entities": [(27, 37, 'PLANT')]
    }),
    ("Care sunt cerințele de bază ale plantei craciunita?", {
        "entities": [(40, 50, 'PLANT')]
    }),
    ("craciunita are o problemă: frunze cazatoare.", {
        "entities": [(27, 43, 'PROBLEM'), (0, 10, 'PLANT')]
    }),
    ("Cum pot rezolva frunze cazatoare la craciunita?", {
        "entities": [(16, 32, 'PROBLEM'), (36, 46, 'PLANT')]
    }),
    ("Am observat frunze cazatoare la craciunita. Ce mă sfătuiți?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 42, 'PLANT')]
    }),
    ("Ce se poate face dacă craciunita suferă de frunze cazatoare?", {
        "entities": [(43, 59, 'PROBLEM'), (22, 32, 'PLANT')]
    }),
    ("frunze cazatoare apare des la craciunita? Cum tratez?", {
        "entities": [(0, 16, 'PROBLEM'), (30, 40, 'PLANT')]
    }),
    ("Este frunze cazatoare periculoasă pentru craciunita?", {
        "entities": [(5, 21, 'PROBLEM'), (41, 51, 'PLANT')]
    }),
]

# Lista entitatilor cunoscute
ENTITIES = {
    "PLANT": ['aloe vera', 'bonsai', 'bujor', 'cactus', 'craciunita', 'crin', 'crizantema', 'ficus', 'garoafa', 'iris', 'lalea', 'lavanda', 'liliac', 'magnolie', 'muscata', 'orhidee', 'trandafir', 'tuia'],
    "CARE_ASPECT": ['lumina', 'pamant', 'udare'],
    "PROBLEM": ['boboci care nu se deschid', 'brunificare varfuri', 'cadere frunze', 'crestere alungita', 'crestere lemnoasa', 'frunze cazatoare', 'frunze galbene', 'frunze maro', 'frunze moi', 'frunze patate', 'ingalbenirea frunzelor', 'inghet flori', 'lipsa florilor', 'lipsa inflorire', 'mucegai pe frunze', 'ofilirea florilor', 'pete maronii', 'pete negre', 'pete pe frunze', 'putine flori', 'putrezire baza', 'putrezirea bazei', 'putrezirea bulbilor', 'putrezirea rizomului', 'radacini putrede', 'scoarta deteriorata', 'tulpini scurte']
}
