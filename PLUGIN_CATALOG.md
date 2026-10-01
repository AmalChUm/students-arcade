# Students Arcade Plugin Catalog

This catalog covers the Python files currently in `plugins/` for [issue #24](https://github.com/AmalChUm/students-arcade/issues/24). The launcher in `main.py` imports each module and calls its `run()` function when one exists. Names and authors below come from the files themselves; a nonstandard field is identified explicitly.

| Plugin file | Declared author | Activity name | Input requirements | Output and launcher behavior |
| --- | --- | --- | --- | --- |
| [`David-Chri.py`](plugins/David-Chri.py) | David Christian (`AUTHOR`) | Coin Flipper (`APP_NAME`) | None | `run()` randomly returns Heads or Tails in a `🎱 Coin Flipper says: ...` message. |
| [`Eliadsp.py`](plugins/Eliadsp.py) | Eliad Spraggins (`AUTHOR`) | Card Generator (`APP_NAME`) | None | `run()` randomly chooses a rank from 2 through Ace and a suit, then returns a `🃏 Card Generator says: ...` message. |
| [`Matt-Rak.py`](plugins/Matt-Rak.py) | Matthew Rakay (`Author`, not `AUTHOR`) | Guessing game (`Game_name`, not `APP_NAME`) | Repeated integer guesses when the file is run directly; the prompt suggests 1 through 100 but does not enforce that range. | The standalone game responds with higher/lower hints, rejects nonnumeric input, and reports the number of attempts after a correct guess. It has no `run()`, so `main.py` shows `plugins.Matt-Rak by Unknown author` and skips it. |
| [`Sule_roll.py`](plugins/Sule_roll.py) | Suleman Saddet (`AUTHOR`) | Magic 8-Ball (`APP_NAME`) | None | Despite its name, `run()` returns the sum of two random integers from 1 through 100. Importing the module also prints the author, activity name, and a separate random sum before the launcher calls `run()`. |
| [`gemini_tips.py`](plugins/gemini_tips.py) | Gemini (`AUTHOR`) | Daily Tip Generator (`APP_NAME`) | None | `run()` returns one randomly selected tip from the file's built-in list in a `💡 Tip of the Day: ...` message. |
| [`ginishima.py`](plugins/ginishima.py) | Gaige Szy (`AUTHOR`) | Number Addition (`APP_NAME`) | None | `run()` uses the fixed calculation `18 + 21` and returns `Your total number is: 39.` |
| [`mklupp.py`](plugins/mklupp.py) | Mackenzie Klupp (`AUTHOR`) | D20 roller (`APP_NAME`) | None | `run()` randomly selects a number from 1 through 20 and returns a `🎱 D20 roller rolled at: ...` message. |
| [`sravyasambaturu.py`](plugins/sravyasambaturu.py) | Sravya Sambaturu (`AUTHOR`) | Magic 8-Ball (`APP_NAME`) | None | `run()` randomly returns one of three responses: `Yes, definitely!`, `Ask again later.`, or `Outlook not so good.` |

To update this catalog, compare each row with its linked source file and run `python -X utf8 main.py` from the repository root. The launcher output identifies plugins that run, fail, or are skipped; random results may differ between runs.
