import uvicorn


if __name__ == "__main__":
    port = 8888

    uvicorn.run(
        app="app.api.main:app",
        port=port,
        reload=True,
        server_header=False,
    )
