# Exercise 0 - Space Station Data: Explanation

## What is Pydantic?

Pydantic is a Python library for data validation. You define a model (a class
inheriting from BaseModel), declare fields with types and constraints, and
Pydantic automatically validates any data you try to create an instance with.

## BaseModel

Every Pydantic model inherits from BaseModel:

    class SpaceStation(BaseModel):
        crew_size: int

This alone gives you type checking. If you pass crew_size="hello", Pydantic
will raise a ValidationError.

## Field()

Field() lets you add constraints beyond just the type:

    crew_size: int = Field(..., ge=1, le=20)

- `...` means the field is required (no default)
- `ge=1` means "greater than or equal to 1"
- `le=20` means "less than or equal to 20"
- `min_length`, `max_length` work the same for strings

## Optional fields

    notes: Optional[str] = Field(default=None, max_length=200)

Optional means the field can be None. The default=None means it's not
required when creating the model.

## DateTime automatic conversion

Pydantic automatically converts ISO 8601 strings to datetime objects:

    last_maintenance="2024-01-15T10:30:00"  # string -> datetime automatically

This is one of Pydantic's most useful features for APIs and data pipelines.

## ValidationError

When data is invalid, Pydantic raises ValidationError with detailed messages.
Always catch it with:

    try:
        station = SpaceStation(crew_size=25, ...)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
