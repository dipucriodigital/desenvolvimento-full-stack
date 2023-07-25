from models import _async_main
import asyncio

if __name__ == "__main__":
    print("Dropping and re/creating tables")
    asyncio.run(_async_main())
    print("Done.")
