# Set generat automat pentru antrenare
TRAINING_DATA = [
    ("Cum ud orhidee?", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la orhidee?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 38, 'PLANT')]
    }),
    ("Care e frecventa udarii la orhidee?", {
        "entities": [(27, 34, 'PLANT')]
    }),
    ("Ce fel de lumina prefera orhidee?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 32, 'PLANT')]
    }),
    ("Cata lumina are nevoie orhidee?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 30, 'PLANT')]
    }),
    ("Unde pun orhidee pentru o lumina buna?", {
        "entities": [(26, 32, 'CARE_ASPECT'), (9, 16, 'PLANT')]
    }),
    ("In ce mediu palntez orhidee?", {
        "entities": [(20, 27, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru orhidee?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui orhidee?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 39, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre orhidee?", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Cum se ingrijeste orhidee?", {
        "entities": [(18, 25, 'PLANT')]
    }),
    ("Informatii generale despre orhidee.", {
        "entities": [(27, 34, 'PLANT')]
    }),
    ("Cum cresc orhidee?", {
        "entities": [(10, 17, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru orhidee?", {
        "entities": [(28, 35, 'PLANT')]
    }),
    ("orhidee are problema: frunze galbene.", {
        "entities": [(22, 36, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum rezolv frunze galbene la orhidee?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 36, 'PLANT')]
    }),
    ("Am observat frunze galbene la orhidee. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("orhidee are problema: radacini putrede.", {
        "entities": [(22, 38, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum rezolv radacini putrede la orhidee?", {
        "entities": [(11, 27, 'PROBLEM'), (31, 38, 'PLANT')]
    }),
    ("Am observat radacini putrede la orhidee. Ce fac?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Cum ud ficus?", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la ficus?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 36, 'PLANT')]
    }),
    ("Care e frecventa udarii la ficus?", {
        "entities": [(27, 32, 'PLANT')]
    }),
    ("Ce fel de lumina prefera ficus?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 30, 'PLANT')]
    }),
    ("Cata lumina are nevoie ficus?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 28, 'PLANT')]
    }),
    ("Unde pun ficus pentru o lumina buna?", {
        "entities": [(24, 30, 'CARE_ASPECT'), (9, 14, 'PLANT')]
    }),
    ("In ce mediu palntez ficus?", {
        "entities": [(20, 25, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru ficus?", {
        "entities": [(25, 30, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui ficus?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 37, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre ficus?", {
        "entities": [(26, 31, 'PLANT')]
    }),
    ("Cum se ingrijeste ficus?", {
        "entities": [(18, 23, 'PLANT')]
    }),
    ("Informatii generale despre ficus.", {
        "entities": [(27, 32, 'PLANT')]
    }),
    ("Cum cresc ficus?", {
        "entities": [(10, 15, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru ficus?", {
        "entities": [(28, 33, 'PLANT')]
    }),
    ("ficus are problema: cadere frunze.", {
        "entities": [(20, 33, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv cadere frunze la ficus?", {
        "entities": [(11, 24, 'PROBLEM'), (28, 33, 'PLANT')]
    }),
    ("Am observat cadere frunze la ficus. Ce fac?", {
        "entities": [(12, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("ficus are problema: frunze galbene.", {
        "entities": [(20, 34, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv frunze galbene la ficus?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Am observat frunze galbene la ficus. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Cum ud trandafir?", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la trandafir?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 40, 'PLANT')]
    }),
    ("Care e frecventa udarii la trandafir?", {
        "entities": [(27, 36, 'PLANT')]
    }),
    ("Ce fel de lumina prefera trandafir?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 34, 'PLANT')]
    }),
    ("Cata lumina are nevoie trandafir?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 32, 'PLANT')]
    }),
    ("Unde pun trandafir pentru o lumina buna?", {
        "entities": [(28, 34, 'CARE_ASPECT'), (9, 18, 'PLANT')]
    }),
    ("In ce mediu palntez trandafir?", {
        "entities": [(20, 29, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru trandafir?", {
        "entities": [(25, 34, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui trandafir?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 41, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre trandafir?", {
        "entities": [(26, 35, 'PLANT')]
    }),
    ("Cum se ingrijeste trandafir?", {
        "entities": [(18, 27, 'PLANT')]
    }),
    ("Informatii generale despre trandafir.", {
        "entities": [(27, 36, 'PLANT')]
    }),
    ("Cum cresc trandafir?", {
        "entities": [(10, 19, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru trandafir?", {
        "entities": [(28, 37, 'PLANT')]
    }),
    ("trandafir are problema: frunze galbene.", {
        "entities": [(24, 38, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum rezolv frunze galbene la trandafir?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 38, 'PLANT')]
    }),
    ("Am observat frunze galbene la trandafir. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 39, 'PLANT')]
    }),
    ("trandafir are problema: pete negre.", {
        "entities": [(24, 34, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum rezolv pete negre la trandafir?", {
        "entities": [(11, 21, 'PROBLEM'), (25, 34, 'PLANT')]
    }),
    ("Am observat pete negre la trandafir. Ce fac?", {
        "entities": [(12, 22, 'PROBLEM'), (26, 35, 'PLANT')]
    }),
    ("Cum ud crin?", {
        "entities": [(7, 11, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la crin?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 35, 'PLANT')]
    }),
    ("Care e frecventa udarii la crin?", {
        "entities": [(27, 31, 'PLANT')]
    }),
    ("Ce fel de lumina prefera crin?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 29, 'PLANT')]
    }),
    ("Cata lumina are nevoie crin?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 27, 'PLANT')]
    }),
    ("Unde pun crin pentru o lumina buna?", {
        "entities": [(23, 29, 'CARE_ASPECT'), (9, 13, 'PLANT')]
    }),
    ("In ce mediu palntez crin?", {
        "entities": [(20, 24, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru crin?", {
        "entities": [(25, 29, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui crin?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 36, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre crin?", {
        "entities": [(26, 30, 'PLANT')]
    }),
    ("Cum se ingrijeste crin?", {
        "entities": [(18, 22, 'PLANT')]
    }),
    ("Informatii generale despre crin.", {
        "entities": [(27, 31, 'PLANT')]
    }),
    ("Cum cresc crin?", {
        "entities": [(10, 14, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru crin?", {
        "entities": [(28, 32, 'PLANT')]
    }),
    ("crin are problema: ingalbenirea frunzelor.", {
        "entities": [(19, 41, 'PROBLEM'), (0, 4, 'PLANT')]
    }),
    ("Cum rezolv ingalbenirea frunzelor la crin?", {
        "entities": [(11, 33, 'PROBLEM'), (37, 41, 'PLANT')]
    }),
    ("Am observat ingalbenirea frunzelor la crin. Ce fac?", {
        "entities": [(12, 34, 'PROBLEM'), (38, 42, 'PLANT')]
    }),
    ("crin are problema: lipsa inflorire.", {
        "entities": [(19, 34, 'PROBLEM'), (0, 4, 'PLANT')]
    }),
    ("Cum rezolv lipsa inflorire la crin?", {
        "entities": [(11, 26, 'PROBLEM'), (30, 34, 'PLANT')]
    }),
    ("Am observat lipsa inflorire la crin. Ce fac?", {
        "entities": [(12, 27, 'PROBLEM'), (31, 35, 'PLANT')]
    }),
    ("Cum ud muscata?", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la muscata?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 38, 'PLANT')]
    }),
    ("Care e frecventa udarii la muscata?", {
        "entities": [(27, 34, 'PLANT')]
    }),
    ("Ce fel de lumina prefera muscata?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 32, 'PLANT')]
    }),
    ("Cata lumina are nevoie muscata?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 30, 'PLANT')]
    }),
    ("Unde pun muscata pentru o lumina buna?", {
        "entities": [(26, 32, 'CARE_ASPECT'), (9, 16, 'PLANT')]
    }),
    ("In ce mediu palntez muscata?", {
        "entities": [(20, 27, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru muscata?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui muscata?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 39, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre muscata?", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Cum se ingrijeste muscata?", {
        "entities": [(18, 25, 'PLANT')]
    }),
    ("Informatii generale despre muscata.", {
        "entities": [(27, 34, 'PLANT')]
    }),
    ("Cum cresc muscata?", {
        "entities": [(10, 17, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru muscata?", {
        "entities": [(28, 35, 'PLANT')]
    }),
    ("muscata are problema: frunze galbene.", {
        "entities": [(22, 36, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum rezolv frunze galbene la muscata?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 36, 'PLANT')]
    }),
    ("Am observat frunze galbene la muscata. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("muscata are problema: putine flori.", {
        "entities": [(22, 34, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum rezolv putine flori la muscata?", {
        "entities": [(11, 23, 'PROBLEM'), (27, 34, 'PLANT')]
    }),
    ("Am observat putine flori la muscata. Ce fac?", {
        "entities": [(12, 24, 'PROBLEM'), (28, 35, 'PLANT')]
    }),
    ("Cum ud aloe vera?", {
        "entities": [(7, 16, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la aloe vera?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 40, 'PLANT')]
    }),
    ("Care e frecventa udarii la aloe vera?", {
        "entities": [(27, 36, 'PLANT')]
    }),
    ("Ce fel de lumina prefera aloe vera?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 34, 'PLANT')]
    }),
    ("Cata lumina are nevoie aloe vera?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 32, 'PLANT')]
    }),
    ("Unde pun aloe vera pentru o lumina buna?", {
        "entities": [(28, 34, 'CARE_ASPECT'), (9, 18, 'PLANT')]
    }),
    ("In ce mediu palntez aloe vera?", {
        "entities": [(20, 29, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru aloe vera?", {
        "entities": [(25, 34, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui aloe vera?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 41, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre aloe vera?", {
        "entities": [(26, 35, 'PLANT')]
    }),
    ("Cum se ingrijeste aloe vera?", {
        "entities": [(18, 27, 'PLANT')]
    }),
    ("Informatii generale despre aloe vera.", {
        "entities": [(27, 36, 'PLANT')]
    }),
    ("Cum cresc aloe vera?", {
        "entities": [(10, 19, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru aloe vera?", {
        "entities": [(28, 37, 'PLANT')]
    }),
    ("aloe vera are problema: frunze maro.", {
        "entities": [(24, 35, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum rezolv frunze maro la aloe vera?", {
        "entities": [(11, 22, 'PROBLEM'), (26, 35, 'PLANT')]
    }),
    ("Am observat frunze maro la aloe vera. Ce fac?", {
        "entities": [(12, 23, 'PROBLEM'), (27, 36, 'PLANT')]
    }),
    ("aloe vera are problema: frunze moi.", {
        "entities": [(24, 34, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum rezolv frunze moi la aloe vera?", {
        "entities": [(11, 21, 'PROBLEM'), (25, 34, 'PLANT')]
    }),
    ("Am observat frunze moi la aloe vera. Ce fac?", {
        "entities": [(12, 22, 'PROBLEM'), (26, 35, 'PLANT')]
    }),
    ("aloe vera are problema: putrezirea bazei.", {
        "entities": [(24, 40, 'PROBLEM'), (0, 9, 'PLANT')]
    }),
    ("Cum rezolv putrezirea bazei la aloe vera?", {
        "entities": [(11, 27, 'PROBLEM'), (31, 40, 'PLANT')]
    }),
    ("Am observat putrezirea bazei la aloe vera. Ce fac?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 41, 'PLANT')]
    }),
    ("Cum ud cactus?", {
        "entities": [(7, 13, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la cactus?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 37, 'PLANT')]
    }),
    ("Care e frecventa udarii la cactus?", {
        "entities": [(27, 33, 'PLANT')]
    }),
    ("Ce fel de lumina prefera cactus?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 31, 'PLANT')]
    }),
    ("Cata lumina are nevoie cactus?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 29, 'PLANT')]
    }),
    ("Unde pun cactus pentru o lumina buna?", {
        "entities": [(25, 31, 'CARE_ASPECT'), (9, 15, 'PLANT')]
    }),
    ("In ce mediu palntez cactus?", {
        "entities": [(20, 26, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru cactus?", {
        "entities": [(25, 31, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui cactus?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 38, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre cactus?", {
        "entities": [(26, 32, 'PLANT')]
    }),
    ("Cum se ingrijeste cactus?", {
        "entities": [(18, 24, 'PLANT')]
    }),
    ("Informatii generale despre cactus.", {
        "entities": [(27, 33, 'PLANT')]
    }),
    ("Cum cresc cactus?", {
        "entities": [(10, 16, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru cactus?", {
        "entities": [(28, 34, 'PLANT')]
    }),
    ("cactus are problema: putrezire baza.", {
        "entities": [(21, 35, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum rezolv putrezire baza la cactus?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 35, 'PLANT')]
    }),
    ("Am observat putrezire baza la cactus. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 36, 'PLANT')]
    }),
    ("cactus are problema: crestere alungita.", {
        "entities": [(21, 38, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum rezolv crestere alungita la cactus?", {
        "entities": [(11, 28, 'PROBLEM'), (32, 38, 'PLANT')]
    }),
    ("Am observat crestere alungita la cactus. Ce fac?", {
        "entities": [(12, 29, 'PROBLEM'), (33, 39, 'PLANT')]
    }),
    ("cactus are problema: pete maronii.", {
        "entities": [(21, 33, 'PROBLEM'), (0, 6, 'PLANT')]
    }),
    ("Cum rezolv pete maronii la cactus?", {
        "entities": [(11, 23, 'PROBLEM'), (27, 33, 'PLANT')]
    }),
    ("Am observat pete maronii la cactus. Ce fac?", {
        "entities": [(12, 24, 'PROBLEM'), (28, 34, 'PLANT')]
    }),
    ("Cum ud lavanda?", {
        "entities": [(7, 14, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la lavanda?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 38, 'PLANT')]
    }),
    ("Care e frecventa udarii la lavanda?", {
        "entities": [(27, 34, 'PLANT')]
    }),
    ("Ce fel de lumina prefera lavanda?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 32, 'PLANT')]
    }),
    ("Cata lumina are nevoie lavanda?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 30, 'PLANT')]
    }),
    ("Unde pun lavanda pentru o lumina buna?", {
        "entities": [(26, 32, 'CARE_ASPECT'), (9, 16, 'PLANT')]
    }),
    ("In ce mediu palntez lavanda?", {
        "entities": [(20, 27, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru lavanda?", {
        "entities": [(25, 32, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui lavanda?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 39, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre lavanda?", {
        "entities": [(26, 33, 'PLANT')]
    }),
    ("Cum se ingrijeste lavanda?", {
        "entities": [(18, 25, 'PLANT')]
    }),
    ("Informatii generale despre lavanda.", {
        "entities": [(27, 34, 'PLANT')]
    }),
    ("Cum cresc lavanda?", {
        "entities": [(10, 17, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru lavanda?", {
        "entities": [(28, 35, 'PLANT')]
    }),
    ("lavanda are problema: radacini putrede.", {
        "entities": [(22, 38, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum rezolv radacini putrede la lavanda?", {
        "entities": [(11, 27, 'PROBLEM'), (31, 38, 'PLANT')]
    }),
    ("Am observat radacini putrede la lavanda. Ce fac?", {
        "entities": [(12, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("lavanda are problema: crestere lemnoasa.", {
        "entities": [(22, 39, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum rezolv crestere lemnoasa la lavanda?", {
        "entities": [(11, 28, 'PROBLEM'), (32, 39, 'PLANT')]
    }),
    ("Am observat crestere lemnoasa la lavanda. Ce fac?", {
        "entities": [(12, 29, 'PROBLEM'), (33, 40, 'PLANT')]
    }),
    ("lavanda are problema: frunze galbene.", {
        "entities": [(22, 36, 'PROBLEM'), (0, 7, 'PLANT')]
    }),
    ("Cum rezolv frunze galbene la lavanda?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 36, 'PLANT')]
    }),
    ("Am observat frunze galbene la lavanda. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 37, 'PLANT')]
    }),
    ("Cum ud lalea?", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la lalea?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 36, 'PLANT')]
    }),
    ("Care e frecventa udarii la lalea?", {
        "entities": [(27, 32, 'PLANT')]
    }),
    ("Ce fel de lumina prefera lalea?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 30, 'PLANT')]
    }),
    ("Cata lumina are nevoie lalea?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 28, 'PLANT')]
    }),
    ("Unde pun lalea pentru o lumina buna?", {
        "entities": [(24, 30, 'CARE_ASPECT'), (9, 14, 'PLANT')]
    }),
    ("In ce mediu palntez lalea?", {
        "entities": [(20, 25, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru lalea?", {
        "entities": [(25, 30, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui lalea?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 37, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre lalea?", {
        "entities": [(26, 31, 'PLANT')]
    }),
    ("Cum se ingrijeste lalea?", {
        "entities": [(18, 23, 'PLANT')]
    }),
    ("Informatii generale despre lalea.", {
        "entities": [(27, 32, 'PLANT')]
    }),
    ("Cum cresc lalea?", {
        "entities": [(10, 15, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru lalea?", {
        "entities": [(28, 33, 'PLANT')]
    }),
    ("lalea are problema: lipsa inflorire.", {
        "entities": [(20, 35, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv lipsa inflorire la lalea?", {
        "entities": [(11, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Am observat lipsa inflorire la lalea. Ce fac?", {
        "entities": [(12, 27, 'PROBLEM'), (31, 36, 'PLANT')]
    }),
    ("lalea are problema: tulpini scurte.", {
        "entities": [(20, 34, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv tulpini scurte la lalea?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("Am observat tulpini scurte la lalea. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("lalea are problema: putrezirea bulbilor.", {
        "entities": [(20, 39, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv putrezirea bulbilor la lalea?", {
        "entities": [(11, 30, 'PROBLEM'), (34, 39, 'PLANT')]
    }),
    ("Am observat putrezirea bulbilor la lalea. Ce fac?", {
        "entities": [(12, 31, 'PROBLEM'), (35, 40, 'PLANT')]
    }),
    ("Cum ud bujor?", {
        "entities": [(7, 12, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la bujor?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 36, 'PLANT')]
    }),
    ("Care e frecventa udarii la bujor?", {
        "entities": [(27, 32, 'PLANT')]
    }),
    ("Ce fel de lumina prefera bujor?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 30, 'PLANT')]
    }),
    ("Cata lumina are nevoie bujor?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 28, 'PLANT')]
    }),
    ("Unde pun bujor pentru o lumina buna?", {
        "entities": [(24, 30, 'CARE_ASPECT'), (9, 14, 'PLANT')]
    }),
    ("In ce mediu palntez bujor?", {
        "entities": [(20, 25, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru bujor?", {
        "entities": [(25, 30, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui bujor?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 37, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre bujor?", {
        "entities": [(26, 31, 'PLANT')]
    }),
    ("Cum se ingrijeste bujor?", {
        "entities": [(18, 23, 'PLANT')]
    }),
    ("Informatii generale despre bujor.", {
        "entities": [(27, 32, 'PLANT')]
    }),
    ("Cum cresc bujor?", {
        "entities": [(10, 15, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru bujor?", {
        "entities": [(28, 33, 'PLANT')]
    }),
    ("bujor are problema: lipsa inflorire.", {
        "entities": [(20, 35, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv lipsa inflorire la bujor?", {
        "entities": [(11, 26, 'PROBLEM'), (30, 35, 'PLANT')]
    }),
    ("Am observat lipsa inflorire la bujor. Ce fac?", {
        "entities": [(12, 27, 'PROBLEM'), (31, 36, 'PLANT')]
    }),
    ("bujor are problema: frunze patate.", {
        "entities": [(20, 33, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv frunze patate la bujor?", {
        "entities": [(11, 24, 'PROBLEM'), (28, 33, 'PLANT')]
    }),
    ("Am observat frunze patate la bujor. Ce fac?", {
        "entities": [(12, 25, 'PROBLEM'), (29, 34, 'PLANT')]
    }),
    ("bujor are problema: boboci care nu se deschid.", {
        "entities": [(20, 45, 'PROBLEM'), (0, 5, 'PLANT')]
    }),
    ("Cum rezolv boboci care nu se deschid la bujor?", {
        "entities": [(11, 36, 'PROBLEM'), (40, 45, 'PLANT')]
    }),
    ("Am observat boboci care nu se deschid la bujor. Ce fac?", {
        "entities": [(12, 37, 'PROBLEM'), (41, 46, 'PLANT')]
    }),
    ("Cum ud magnolie?", {
        "entities": [(7, 15, 'PLANT')]
    }),
    ("Ce metoda de udare folosesc la magnolie?", {
        "entities": [(13, 18, 'CARE_ASPECT'), (31, 39, 'PLANT')]
    }),
    ("Care e frecventa udarii la magnolie?", {
        "entities": [(27, 35, 'PLANT')]
    }),
    ("Ce fel de lumina prefera magnolie?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (25, 33, 'PLANT')]
    }),
    ("Cata lumina are nevoie magnolie?", {
        "entities": [(5, 11, 'CARE_ASPECT'), (23, 31, 'PLANT')]
    }),
    ("Unde pun magnolie pentru o lumina buna?", {
        "entities": [(27, 33, 'CARE_ASPECT'), (9, 17, 'PLANT')]
    }),
    ("In ce mediu palntez magnolie?", {
        "entities": [(20, 28, 'PLANT')]
    }),
    ("Ce sol e potrivit pentru magnolie?", {
        "entities": [(25, 33, 'PLANT')]
    }),
    ("Ce fel de pamant ii trebuie lui magnolie?", {
        "entities": [(10, 16, 'CARE_ASPECT'), (32, 40, 'PLANT')]
    }),
    ("Ce trebuie sa stiu despre magnolie?", {
        "entities": [(26, 34, 'PLANT')]
    }),
    ("Cum se ingrijeste magnolie?", {
        "entities": [(18, 26, 'PLANT')]
    }),
    ("Informatii generale despre magnolie.", {
        "entities": [(27, 35, 'PLANT')]
    }),
    ("Cum cresc magnolie?", {
        "entities": [(10, 18, 'PLANT')]
    }),
    ("Ce recomandari aveti pentru magnolie?", {
        "entities": [(28, 36, 'PLANT')]
    }),
    ("magnolie are problema: inghet flori.", {
        "entities": [(23, 35, 'PROBLEM'), (0, 8, 'PLANT')]
    }),
    ("Cum rezolv inghet flori la magnolie?", {
        "entities": [(11, 23, 'PROBLEM'), (27, 35, 'PLANT')]
    }),
    ("Am observat inghet flori la magnolie. Ce fac?", {
        "entities": [(12, 24, 'PROBLEM'), (28, 36, 'PLANT')]
    }),
    ("magnolie are problema: frunze galbene.", {
        "entities": [(23, 37, 'PROBLEM'), (0, 8, 'PLANT')]
    }),
    ("Cum rezolv frunze galbene la magnolie?", {
        "entities": [(11, 25, 'PROBLEM'), (29, 37, 'PLANT')]
    }),
    ("Am observat frunze galbene la magnolie. Ce fac?", {
        "entities": [(12, 26, 'PROBLEM'), (30, 38, 'PLANT')]
    }),
    ("magnolie are problema: scoarta deteriorata.", {
        "entities": [(23, 42, 'PROBLEM'), (0, 8, 'PLANT')]
    }),
    ("Cum rezolv scoarta deteriorata la magnolie?", {
        "entities": [(11, 30, 'PROBLEM'), (34, 42, 'PLANT')]
    }),
    ("Am observat scoarta deteriorata la magnolie. Ce fac?", {
        "entities": [(12, 31, 'PROBLEM'), (35, 43, 'PLANT')]
    }),
]

# Lista entitatilor cunoscute
ENTITIES = {
    "PLANT": ['aloe vera', 'bujor', 'cactus', 'crin', 'ficus', 'lalea', 'lavanda', 'magnolie', 'muscata', 'orhidee', 'trandafir'],
    "CARE_ASPECT": ['lumina', 'pamant', 'udare'],
    "PROBLEM": ['boboci care nu se deschid', 'cadere frunze', 'crestere alungita', 'crestere lemnoasa', 'frunze galbene', 'frunze maro', 'frunze moi', 'frunze patate', 'ingalbenirea frunzelor', 'inghet flori', 'lipsa inflorire', 'pete maronii', 'pete negre', 'putine flori', 'putrezire baza', 'putrezirea bazei', 'putrezirea bulbilor', 'radacini putrede', 'scoarta deteriorata', 'tulpini scurte']
}
