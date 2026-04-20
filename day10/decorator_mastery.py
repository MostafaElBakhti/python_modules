import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # If first arg is not int, it's likely 'self' — find power in kwargs or last arg
            if isinstance(args[0], int):
                power = args[0]
            else:
                power = kwargs.get('power', args[-1])
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying..."
                        f" (attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball_cast() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball_cast()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    attempt_count = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise RuntimeError("Spell unstable!")
        return "Waaaaaaagh spelled !"

    result = retry_spell(max_attempts=3)(
        lambda: (_ for _ in ()).throw(RuntimeError("always fails"))
    )()
    print(result)

    attempt_count[0] = 0

    @retry_spell(max_attempts=3)
    def eventually_works() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise RuntimeError("Not yet...")
        return "Waaaaaaagh spelled !"

    print(eventually_works())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Thunder", 5))
