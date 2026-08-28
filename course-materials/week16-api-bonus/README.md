# Week 16 Bonus - Public API Integration with Python

This optional pack introduces real-world API calls using Python and the `requests` library.

## Learning goals

- Send HTTP `GET` requests to public endpoints.
- Read and parse JSON responses.
- Handle common response outcomes (`200`, `401`, `404`, `429`, `5xx`).
- Build one small, personal "data explorer" script.

## Install requirement

```bash
pip install requests
```

## Curated API list (classroom-friendly)

### 1. NASA Open APIs

- Docs: <https://api.nasa.gov/>
- Auth: API key required for normal use. `DEMO_KEY` works for exploration with lower limits.
- Good starter endpoints:
  - APOD: `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`
  - Mars rover photos (archived note on portal; verify current status before class):
    `https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY`

### 2. SpaceX API (community-maintained)

- Docs: <https://github.com/r-spacex/SpaceX-API/tree/master/docs>
- Auth: None
- Suggested base: `https://api.spacexdata.com/v4`
- Good starter endpoint:
  - Latest launch: `https://api.spacexdata.com/v4/launches/latest`
- Note: This API is not official SpaceX infrastructure; availability may vary.

### 3. PokeAPI

- Docs: <https://pokeapi.co/docs/v2>
- Auth: None
- Good starter endpoint:
  - Pokemon by name: `https://pokeapi.co/api/v2/pokemon/ditto`

### 4. TMDB (The Movie Database)

- Docs: <https://developer.themoviedb.org/docs/getting-started>
- Auth: API key required
- Good starter endpoint pattern:
  - Trending: `https://api.themoviedb.org/3/trending/movie/day?api_key=YOUR_TMDB_KEY`

### 5. Rick and Morty API

- Docs: <https://rickandmortyapi.com/documentation>
- Auth: None
- Good starter endpoints:
  - Character: `https://rickandmortyapi.com/api/character/2`
  - Episode: `https://rickandmortyapi.com/api/episode/1`

### 6. OpenWeatherMap

- Docs: <https://openweathermap.org/api>
- Auth: API key required
- Good starter endpoint pattern:
  - Current weather: `https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_OWM_KEY&units=metric`

### 7. REST Countries

- Docs: <https://restcountries.com/docs>
- Auth: Check current plan/docs status before class (service and tiers have evolved).
- Common free-style endpoint used in many examples:
  - `https://restcountries.com/v3.1/name/canada`

## Safety and reliability checklist for students

1. Never paste private API keys into public repos.
2. Store keys in environment variables when possible.
3. Add timeout to requests.
4. Handle non-200 status codes gracefully.
5. Cache or limit repeated requests.
6. Read each API's terms and rate limits.

## Included files

- `pokemon_requests_example.py` - fixed working starter using PokeAPI.
- `api_project_ideas.md` - project prompts using the curated APIs.
- `api_error_handling_template.py` - reusable request helper template.
