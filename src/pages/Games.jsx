import GameCard from '../components/GameCard'
import './Games.css'

// Game data - in a real app this would come from a database
const games = [
    {
        id: 'basketball',
        title: '🏀 Flick Hoops',
        description: 'Flick the ball into the hoop! Test your aim in this addictive basketball game.',
        thumbnail: '/games/basketball/thumbnail.png',
        players: '1-2 Players',
        featured: true
    },
    {
        id: 'coming-soon-1',
        title: '🎯 Target Practice',
        description: 'Aim and shoot at moving targets. Coming soon!',
        thumbnail: null,
        players: 'Coming Soon'
    },
    {
        id: 'coming-soon-2',
        title: '🏓 Pong Masters',
        description: 'Classic pong with a modern twist. Coming soon!',
        thumbnail: null,
        players: 'Coming Soon'
    }
]

function Games() {
    const featuredGame = games.find(g => g.featured)
    const otherGames = games.filter(g => !g.featured)

    return (
        <div className="games-page">
            <div className="games-header">
                <h1>🎮 Games</h1>
                <p>Pick a game and start playing with friends!</p>
            </div>

            {/* Featured Game */}
            {featuredGame && (
                <div className="featured-section">
                    <h2 className="section-title">⭐ Featured</h2>
                    <div className="featured-game">
                        <GameCard game={featuredGame} />
                    </div>
                </div>
            )}

            {/* All Games */}
            <div className="games-section">
                <h2 className="section-title">All Games</h2>
                <div className="games-grid">
                    {otherGames.map((game) => (
                        <GameCard key={game.id} game={game} />
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Games
