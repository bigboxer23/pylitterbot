import asyncio

from pylitterbot import Account

# Set email and password for initial authentication.
username = "###"
password = "###"

async def main():
    account = Account()
    try:
        await account.connect(username=username, password=password, load_robots=True)
        for robot in account.robots:
            await robot.start_cleaning()
    finally:
        await account.disconnect()

if __name__ == "__main__":
    asyncio.run(main())