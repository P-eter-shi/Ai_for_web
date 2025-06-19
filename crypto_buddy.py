crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10,
        "description": "The original cryptocurrency with strong store-of-value properties but high energy consumption."
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10,
        "description": "A programmable blockchain with smart contract functionality, transitioning to more energy-efficient protocols."
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10,
        "description": "A proof-of-stake blockchain focused on sustainability and peer-reviewed research."
    },
    "Solana": {
        "price_trend": "volatile",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10,
        "description": "High-performance blockchain with low fees, but has faced some network stability issues."
    }
}

def respond_to_query(user_query):
    user_query = user_query.lower()
    response = ""
    disclaimer = "\n\nRemember: Crypto is risky—always do your own research! (DYOR) 🔍"
    
    if any(word in user_query for word in ["trend", "rising", "growing"]):
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        response = f"These cryptos are currently trending up: {', '.join(trending)}. "
        if trending:
            best = max(trending, key=lambda x: crypto_db[x]["market_cap"])
            response += f"\nFor maximum potential, consider {best} as it has both rising value and high market cap! 📈"
    
    elif "sustain" in user_query or "eco" in user_query or "green" in user_query:
        sustainable = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        response = (f"For sustainability, I recommend {sustainable}! 🌱\n"
                   f"Sustainability score: {crypto_db[sustainable]['sustainability_score']*10}/10\n"
                   f"Energy use: {crypto_db[sustainable]['energy_use']}\n"
                   f"{crypto_db[sustainable]['description']}")
    
    elif "long-term" in user_query or "future" in user_query:
        balanced = max(crypto_db, key=lambda x: (crypto_db[x]["sustainability_score"]*0.6 + 
                                               (10 if crypto_db[x]["price_trend"]=="rising" else 5) +
                                               (10 if crypto_db[x]["market_cap"]=="high" else 5)))
        response = (f"For long-term growth, consider {balanced}! 🚀\n"
                   f"It combines good sustainability ({crypto_db[balanced]['sustainability_score']*10}/10) "
                   f"with {'rising' if crypto_db[balanced]['price_trend']=='rising' else 'stable'} value "
                   f"and {crypto_db[balanced]['market_cap']} market cap.\n"
                   f"{crypto_db[balanced]['description']}")
    
    elif "stable" in user_query or "safe" in user_query:
        stable_coins = [coin for coin in crypto_db if crypto_db[coin]["market_cap"] == "high"]
        response = f"For more stability, look at large-cap coins: {', '.join(stable_coins)}. "
        response += "These have more established networks and liquidity. ⚖️"
    
    else:
        response = ("I can help you find cryptos based on:\n"
                   "- Trends and growth potential 📈\n"
                   "- Sustainability and energy efficiency 🌱\n"
                   "- Long-term potential 🚀\n"
                   "- Stability and safety ⚖️\n"
                   "Ask me anything about these aspects!")
    
    return response + disclaimer
print("Welcome to cryptobuddy, how may i assist you?")
user_query=input("Your query:  " )
respond=respond_to_query(user_query)
print(respond)