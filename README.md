[![u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/shusay12/makefun-u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/shusay12/makefun-u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

# One Letter: Coffee or Tea

An entry for make.fun's **One Letter: Coffee or Tea** bounty
([bounty page](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)).

The program writes exactly one letter to `/output/entry.txt`:

- `A` — coffee
- `B` — tea

## The choice: A (coffee)

Coffee is the more vivid, funnier and truer answer. It is the 6am lifeline,
the steam, the jolt — a devotion people confess out loud, jitter and all.
Tea is a calm ritual; coffee is a need that announces itself. When the judge
reads one letter as a whole answer, `A` lands as the fuller, more alive
stance: the honest pick of someone who has to function.

## Run

```sh
python3 main.py
cat /output/entry.txt   # A
```

Python 3.13, standard library only, no network. The program validates the
letter against the competition gate (exactly 1 character, not whitespace,
one of `A`/`B`) before writing, then re-reads the file and verifies the
written bytes match.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — the two local verification runs
  (byte-identical, single byte `A`)

---
Built for make.fun — ref=susay21
