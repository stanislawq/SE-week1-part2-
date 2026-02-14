"""
Main application module.
"""
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    """
    Main entry point of the application.
    """
    console = Console()
    console.print("NHL statistics by nationality", style="bold white")

    seasons = [
        "2018-19", "2019-20", "2020-21", "2021-22",
        "2022-23", "2023-24", "2024-25", "2025-26"
    ]

    season_prompt = (
        f"Season [bold cyan][[/bold cyan][bold magenta]"
        f"{'/'.join(seasons)}"
        f"[/bold magenta][bold cyan]][/bold cyan]"
    )
    season = Prompt.ask(season_prompt, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    countries = [
        "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
        "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
        "NOR", "UZB", "LAT", "AUS"
    ]

    while True:
        country_prompt = (
            f"Nationality [bold cyan][[/bold cyan][bold magenta]"
            f"{'/'.join(countries)}"
            f"[/bold magenta][bold cyan]][/bold cyan] "
            f"[bold cyan]()[/bold cyan]"
        )
        nationality = Prompt.ask(country_prompt)

        if not nationality:
            break

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"[italic]Season {season} players from {nationality}[/italic]")

        table.add_column("Released", style="cyan", no_wrap=True)
        table.add_column("teams", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points)
            )

        console.print(table)


if __name__ == "__main__":
    main()
