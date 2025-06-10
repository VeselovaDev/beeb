import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(
        "src.application:build_app",
        port=int(os.getenv("SERVER_PORT", 1818)),
        host=os.getenv("SERVER_HOST"),
        proxy_headers=True,
        forwarded_allow_ips="*",
        factory=True,
    )
