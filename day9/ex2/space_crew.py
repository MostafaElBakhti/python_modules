from datetime import datetime
from enum import Enum
from typing import List, Self

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leader = False
        for member in self.crew:
            if (
                member.rank == Rank.commander
                or member.rank == Rank.captain
            ):
                has_leader = True
                break
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        for member in self.crew:
            if not member.is_active:
                raise ValueError(
                    f"All crew members must be active. "
                    f"{member.name} is inactive."
                )

        if self.duration_days > 365:
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1
            ratio = experienced_count / len(self.crew)
            if ratio < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced "
                    "crew (5+ years)"
                )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=42,
            specialization="Mission Command",
            years_experience=15,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=35,
            specialization="Navigation",
            years_experience=8,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=28,
            specialization="Engineering",
            years_experience=5,
        ),
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 7, 20, 8, 0, 0),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"  - {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )

    print("=" * 41)

    try:
        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Doomed Mission",
            destination="Moon",
            launch_date=datetime(2024, 8, 1, 8, 0, 0),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="CM010",
                    name="Bob Nobody",
                    rank=Rank.cadet,
                    age=22,
                    specialization="Cleaning",
                    years_experience=0,
                )
            ],
            budget_millions=100.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
