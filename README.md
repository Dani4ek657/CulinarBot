# CulinarBot
Telegram Culinary Bot - Complete Documentation
Bot Overview
This is a comprehensive Telegram culinary assistant bot that provides users with access to a wide variety of recipes organized into intuitive categories. The bot features an interactive menu system with visual keyboard buttons for seamless navigation through different culinary sections, including soups, salads, drinks, desserts, snacks, and holiday-specific recipes. All recipe data is sourced from an external module called Slovar which contains structured information about each dish including names, descriptions, and ingredient lists.

Detailed Function Descriptions
1. menu(update: Update, context: ContextTypes.DEFAULT_TYPE)
Primary Purpose: Serves as the main navigation hub by displaying the primary category selection menu to users.

Key Functionality: Creates a 2x3 grid keyboard layout containing six main culinary categories: Soups🥘, Salads🥗, Drinks☕️🍸, Desserts🍰, Snacks🍢, and Holiday Recipes🥂. The function sends this interactive keyboard to the user along with an invitation message prompting them to select a category of culinary masterpieces they'd like to explore. This function is typically called when users enter the /menu command or return from submenus, establishing the central navigation point for the entire bot experience.

2. start(update: Update, context: ContextTypes.DEFAULT_TYPE)
Primary Purpose: Handles initial bot introduction and provides basic instructions to new users.

Key Functionality: Responds to the /start command by sending a welcoming message that introduces the bot as "the best culinary bot🥠🍚" and provides instructions on how to proceed. The message guides users to enter the /menu command to activate the bot's main functionality. This function serves as the entry point for user interaction, setting the tone for the bot's personality and establishing the initial user experience.

3. handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE)
Primary Purpose: Processes all user interactions with the custom keyboard buttons and manages the complete navigation flow.

Key Functionality: This is the core routing function that handles text messages corresponding to button selections. It performs several critical operations: First, it manages the holiday submenu system by displaying a specialized keyboard for holiday selections (New Year🎄🎅, Easter☦️, Birthday🥳🎉) when users choose "Holiday Recipes🥂" and provides a "Back🔙" button to return to the main menu. Second, it processes category selections by extracting relevant recipe data from the recipes dictionary and formatting it into readable messages with Markdown formatting. For each category (soups, salads, drinks, desserts, snacks), it compiles all recipes including their names, brief descriptions, and detailed ingredient lists with measurements. Third, it handles the holiday-specific recipe displays by accessing nested dictionary structures to present New Year, Easter, and Birthday recipes with the same detailed formatting. The function ensures consistent presentation across all categories with numbered listings, ingredient bullet points, and visual separators for improved readability.

4. main()
Primary Purpose: Configures and launches the Telegram bot application with all necessary handlers and settings.

Key Functionality: This function serves as the application entry point and performs several essential setup tasks: It initializes the bot token (currently empty but designed for secure token management), builds the Telegram application instance using the ApplicationBuilder pattern, and registers all command and message handlers. The handler registration includes the start and menu command handlers for /start and /menu commands respectively, plus a MessageHandler that captures all text input (excluding commands) for button processing. Finally, it starts the bot in polling mode with a console notification and configures it to process all update types. The function includes commented guidance about security best practices for token management, suggesting the use of environment variables for production deployment.

Technical Architecture
The bot leverages the python-telegram-bot library for Telegram API integration and follows a callback-based architecture where each user interaction triggers specific handler functions. Recipe data is decoupled from bot logic through the external Slovar module, allowing for easy updates to culinary content without modifying bot code. The navigation system implements a hierarchical menu structure with one level of submenus for holiday recipes, maintaining simplicity while providing organized access to specialized content.
