from knowledge_base import KnowledgeBase
from experta import KnowledgeEngine, DefFacts, Rule, Fact, MATCH


class PlantExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.kb = KnowledgeBase()
        self.response = None
        self.current_plant = None

    @DefFacts()
    def _initial_facts(self):
        yield Fact(action="start")

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(problem=MATCH.problem),
        Fact(intent="problem"),
    )
    def specific_problem(self, plant, problem):
        problem_info = self.kb.get_problem_details(plant, problem)
        problem_print = problem.replace("_", " ")
        response_parts = []

        if problem_info:
            # Adauga detaliile, daca exista
            if 'detalii' in problem_info and problem_info['detalii']:
                response_parts.append(
                    f"Detalii despre problemă: {problem_info['detalii']}")

            # Adauga cauzele, daca exista
            if 'cauze' in problem_info and problem_info['cauze']:
                response_parts.append(
                    f"Cauze posibile: {', '.join(problem_info['cauze'])}.")

            # Adauga solutiile, daca exista
            if 'solutii' in problem_info and problem_info['solutii']:
                response_parts.append(
                    f"Soluții recomandate: {', '.join(problem_info['solutii'])}")

            if response_parts:
                self.response = f"Pentru {plant} cu problema {problem_print}:\n" + "\n".join(
                    response_parts)
            else:
                self.response = f"Am găsit problema '{problem_print}' la planta {plant}, dar nu am detalii, cauze sau soluții specifice."
        else:
            self.response = f"Nu am informații specifice despre problema '{problem_print}' la planta {plant}."

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(aspect=MATCH.aspect),
        Fact(intent="care"),
    )
    def specific_care(self, plant, aspect):
        care_info = self.kb.get_care_aspect(plant, aspect)
        if care_info:
            self.response = f"Pentru {plant}, referitor la {aspect}: {care_info['detalii']}"
        else:
            self.response = f"Nu am informații specifice despre aspectul '{aspect}' pentru planta {plant}."

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(intent="general")
    )
    def general_care_info(self, plant):
        basic_care = self.kb.get_basic_care(plant)
        if basic_care:
            self.response = (
                f"Pentru {plant}, iată informațiile de bază:\n"
                f"- Udare: {basic_care['udare']['detalii']}\n"
                f"- Lumină: {basic_care['lumina']['detalii']}\n"
                f"- Pământ: {basic_care['pamant']['detalii']}"
            )
        else:
            self.response = f"Nu am informații de bază pentru planta {plant}."

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(aspect="lumina")
    )
    def light_conditions_check(self, plant):
        care_info = self.kb.get_care_aspect(plant, "lumina")
        if care_info:
            self.response = (
                f"Pentru {plant}, cerințele de lumină sunt următoarele:\n"
                f"- Intensitate: {care_info.get('intensitate', 'N/A')}\n"
                f"- Expunere recomandată: {care_info.get('expunere', 'N/A')}\n"
                f"- {care_info['detalii']}"
            )

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(aspect="udare")
    )
    def water_conditions_check(self, plant):
        care_info = self.kb.get_care_aspect(plant, "udare")
        if care_info:
            self.response = (
                f"Pentru {plant}, cerințele de udare sunt următoarele:\n"
                f"- Frecvență: {care_info.get('frecventa', 'N/A')}\n"
                f"- Metoda recomandată: {care_info.get('metoda', 'N/A')}\n"
                f"- {care_info['detalii']}"
            )

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(aspect="pamant")
    )
    def soil_conditions_check(self, plant):
        care_info = self.kb.get_care_aspect(plant, "pamant")
        if care_info:
            self.response = (
                f"Pentru {plant}, cerințele de pămant sunt:\n"
                f"- Tip: {care_info.get('tip', 'N/A')}\n"
                f"- {care_info['detalii']}"
            )

    def get_expert_response(self, entities: dict, intent: str) -> str:
        self.reset()
        self.declare(Fact(action="start"))
        self.declare(Fact(intent=intent))

        if entities.get("PLANT"):
            self.current_plant = entities["PLANT"][0]
            self.declare(Fact(plant=self.current_plant))

        if entities.get("PROBLEM"):
            self.declare(Fact(problem=entities["PROBLEM"][0]))

        if entities.get("CARE_ASPECT"):
            self.declare(Fact(aspect=entities["CARE_ASPECT"][0]))

        self.run()

        if self.response and self.current_plant:
            if self.current_plant.lower() not in self.response.lower():
                # Nu a fost gasita intentia utilizatorului, se afiseaza detalii generale
                basic_care = self.kb.get_basic_care(self.current_plant)
                if basic_care:
                    self.response = (
                        f"Pentru {self.current_plant}, iată informațiile de bază:\n"
                        f"- Udare: {basic_care['udare']['detalii']}\n"
                        f"- Lumină: {basic_care['lumina']['detalii']}\n"
                        f"- Pământ: {basic_care['pamant']['detalii']}"
                    )
        return self.response
