from knowledge_base import KnowledgeBase
from experta import KnowledgeEngine, DefFacts, Rule, Fact, MATCH, AND, OR

class PlantExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.kb = KnowledgeBase()
        self.response = None
        
    @DefFacts()
    def _initial_facts(self):
        yield Fact(action="start")

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(problem=MATCH.problem),
        Fact(intent="problem")
    )
    def specific_problem(self, plant, problem):
        problem_info = self.kb.get_problem_details(plant, problem)
        if problem_info and 'detalii' in problem_info:
            self.response = problem_info['detalii']
        elif problem_info:
            self.response = (
                f"Pentru {plant}, problema {problem} poate fi cauzată de: "
                f"{', '.join(problem_info['cauze'])}.\n"
                f"Soluții recomandate: {', '.join(problem_info['solutii'])}"
            )

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(aspect=MATCH.aspect),
        Fact(intent="care")
    )
    def specific_care(self, plant, aspect):
        care_info = self.kb.get_care_aspect(plant, aspect)
        if care_info:
            self.response = f"Pentru {plant}, referitor la {aspect}: {care_info['detalii']}"


    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(soil_condition="dry"),
        Fact(intent="care")
    )
    def watering_advice_dry_soil(self, plant):
        care_info = self.kb.get_care_aspect(plant, "udare")
        if care_info:
            self.response = (
                f"Observ că solul este uscat. "
                f"Recomandarea pentru {plant}: {care_info['detalii']}"
            )

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
                f"- Substrat: {basic_care['substrat']['detalii']}"
            )

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(problem=MATCH.problem),
        Fact(condition="wet")
    )
    def overwatering_problem(self, plant, problem):
        if problem == "frunze_galbene":
            problem_info = self.kb.get_problem_details(plant, problem)
            if "udare excesiva" in problem_info.get("cauze", []):
                self.response = (
                    f"Am detectat că planta {plant} are frunze galbene și solul este umed. "
                    f"Cel mai probabil cauza este udarea excesivă. "
                    f"Recomandări: {', '.join(problem_info['solutii'])}"
                )

    @Rule(
        Fact(action="start"),
        Fact(plant=MATCH.plant),
        Fact(aspect="lumina"),
        Fact(intent="care")
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
        AND(
            OR(
                Fact(problem="frunze_galbene"),
                Fact(problem="cadere_frunze")
            ),
            Fact(condition="dry")
        )
    )
    def multiple_problems_diagnosis(self, plant):
        response_parts = []
        
        yellow_leaves = self.kb.get_problem_details(plant, "frunze_galbene")
        falling_leaves = self.kb.get_problem_details(plant, "cadere_frunze")
        
        if yellow_leaves and "lumina insuficienta" in yellow_leaves.get("cauze", []):
            response_parts.append(
                f"Frunzele galbene pot fi cauzate de lumină insuficientă. "
                f"Soluții: {', '.join(yellow_leaves['solutii'])}"
            )
            
        if falling_leaves and "udare neregulata" in falling_leaves.get("cauze", []):
            response_parts.append(
                f"Căderea frunzelor poate fi cauzată de udare neregulată. "
                f"Soluții: {', '.join(falling_leaves['solutii'])}"
            )
            
        if response_parts:
            self.response = f"Pentru {plant} am detectat multiple probleme:\n" + "\n".join(response_parts)


    def get_expert_response(self, entities: dict, intent: str) -> str:
        self.reset()
        self.declare(Fact(action="start"))
        self.declare(Fact(intent=intent))
        
        if entities.get("PLANT"):
            self.declare(Fact(plant=entities["PLANT"][0]))
            
        if entities.get("PROBLEM"):
            self.declare(Fact(problem=entities["PROBLEM"][0]))
            
        if entities.get("CARE_ASPECT"):
            self.declare(Fact(aspect=entities["CARE_ASPECT"][0]))
            
        if "uscat" in str(entities).lower():
            self.declare(Fact(soil_condition="dry"))
            
        self.run()
        return self.response