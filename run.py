if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="localhost", port=8080, reload=True)