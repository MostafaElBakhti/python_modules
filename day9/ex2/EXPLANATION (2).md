# Exercise 2 - Space Crew Management: Explanation

## Nested Models

A Pydantic model can contain another Pydantic model as a field:

    class SpaceMission(BaseModel):
        crew: List[CrewMember]

When you create a SpaceMission, Pydantic automatically validates every
CrewMember in the list. If any member is invalid, the whole mission fails.

This is called nested validation — it propagates errors up the chain.

## List with constraints

    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)

This means:
- At least 1 crew member required
- Maximum 12 crew members
- Each item in the list must be a valid CrewMember

## Multi-field validation with @model_validator

The mission rules require checking relationships between fields:

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        # Check if any crew member has high rank
        has_leader = any(
            m.rank in (Rank.commander, Rank.captain)
            for m in self.crew
        )
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or Captain")
        return self

## What happens with inactive crew?

The correction sheet asks: "Create a SpaceMission with one active Commander
and one inactive Captain. What happens?"

Answer: the validator checks ALL crew members for is_active=False.
Even if the mission has a valid commander, one inactive member fails the
whole mission validation.

## default values without Field()

    mission_status: str = "planned"

Simple string default — no Field() needed. Correction sheet tests:
"Try to create a SpaceMission without specifying the status. Is it planned?"

## Over budget

    budget_millions: float = Field(..., ge=1.0, le=10000.0)

Passing budget_millions=99999.0 raises a ValidationError immediately
from Field() before @model_validator even runs. Field constraints always
run first.

## Progression of concepts across exercises

- ex0: Basic BaseModel + Field() constraints
- ex1: @model_validator for cross-field business rules + Enum
- ex2: Nested models (model inside model) + List validation + complex rules
