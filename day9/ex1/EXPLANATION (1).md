# Exercise 1 - Alien Contact Logs: Explanation

## Enum

An Enum defines a fixed set of allowed values for a field:

    class ContactType(Enum):
        radio = "radio"
        visual = "visual"
        physical = "physical"
        telepathic = "telepathic"

If you pass contact_type="unknown", Pydantic rejects it immediately.
Use .value to get the string: ContactType.radio.value == "radio"

## @model_validator(mode='after')

Field() handles simple constraints (min, max, length).
But some rules involve MULTIPLE fields together — that requires
@model_validator:

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        return self

Key rules:
- `mode="after"` means all fields are already validated when this runs
- You access fields via `self.field_name`
- Raise ValueError with a clear message if the rule is broken
- ALWAYS return self at the end

## Why not @validator?

@validator is from Pydantic v1 and is deprecated in v2.
Always use @model_validator(mode='after') in Pydantic v2.

## Optional with max_length

    message_received: Optional[str] = Field(default=None, max_length=500)

This field can be None OR a string up to 500 characters.
Both constraints work together.

## Default values

    is_verified: bool = False

No Field() needed for simple defaults. The value is False unless
explicitly set to True. This is tested in the correction sheet:
"Try to create a contact without specifying is_verified. Is it False?"
