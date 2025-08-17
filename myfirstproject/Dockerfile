FROM astral/uv:python3.11-bookworm-slim
WORKDIR /code
COPY . /code/
RUN uv sync
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT [ "/code/entrypoint.sh" ]