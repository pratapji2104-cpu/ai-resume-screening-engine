from src.agents.planner_agent import PlannerAgent
from src.agents.research_agent import ResearchAgent
from src.agents.analysis_agent import AnalysisAgent
from src.agents.decision_agent import DecisionAgent

from src.memory.short_term_memory import ShortTermMemory
from src.memory.long_term_memory import LongTermMemory


class AgentCoordinator:

    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.analyst = AnalysisAgent()
        self.decision_maker = DecisionAgent()

        self.short_term_memory = ShortTermMemory()
        self.long_term_memory = LongTermMemory()

    def coordinate(
        self,
        resume_text,
        job_role,
        resume_analysis,
        job_info,
        job_description_requirements,
        skill_matching
    ):

        # Store current workflow information
        self.short_term_memory.store(
            "resume_text",
            resume_text
        )

        self.short_term_memory.store(
            "job_role",
            job_role
        )

        self.short_term_memory.store(
            "skill_matching",
            skill_matching
        )

        # Store persistent job information
        self.long_term_memory.store(
            "job_role",
            job_role
        )

        self.long_term_memory.store(
            "job_requirements",
            job_info
        )

        # Agent 1: Create workflow plan
        plan = self.planner.create_plan(
            resume_text,
            job_role
        )

        # Agent 2: Collect job information
        research = self.researcher.collect_information(
            job_info,
            job_description_requirements
        )

        # Agent 3: Analyze resume and skill matching
        analysis = self.analyst.analyze(
            resume_analysis,
            skill_matching
        )

        # Agent 4: Make final decision
        decision = self.decision_maker.make_decision(
            analysis
        )

        # Return collaborative workflow result
        return {
            "plan": plan,
            "research": research,
            "analysis": analysis,
            "decision": decision,
            "short_term_memory": self.short_term_memory.get_all(),
            "long_term_memory": self.long_term_memory.get_all()
        }