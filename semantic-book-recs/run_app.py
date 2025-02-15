import uvicorn


if __name__ == "__main__":
    port = 3000

    uvicorn.run(
        host="0.0.0.0",
        app="app.api.main:app",
        port=port,
        reload=True,
        server_header=False,
    )
