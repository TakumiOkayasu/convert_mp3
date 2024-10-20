FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# 基本的なパッケージのインストールと不要なファイルの削除
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    sudo \
    ssh \
    build-essential \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ユーザー情報設定
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# ユーザーの作成とsudo権限の付与（ユーザーが存在していれば実行されない）
RUN if ! getent group $USER_GID; then groupadd --gid $USER_GID $USERNAME; fi \
    && if ! id -u $USERNAME > /dev/null 2>&1; then useradd --uid $USER_UID --gid $USER_GID -m $USERNAME; fi \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# gitの補完スクリプトをダウンロードし、シェルに追加
RUN curl -o /usr/share/bash-completion/completions/git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh \
    && curl -o /usr/share/bash-completion/completions/git-completion.bash https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash

# ~/.bashrcにPS1とunset PROMPT_COMMANDを追記
RUN echo "source /usr/share/bash-completion/completions/git-completion.bash" >> /home/$USERNAME/.bashrc \
    && echo "source /usr/share/bash-completion/completions/git-prompt.sh" >> /home/$USERNAME/.bashrc \
    && echo "GIT_PS1_SHOWDIRTYSTATE=true" >> /home/$USERNAME/.bashrc \
    && echo "GIT_PS1_SHOWUNTRACKEDFILES=true" >> /home/$USERNAME/.bashrc \
    && echo "GIT_PS1_SHOWUPSTREAM=auto" >> /home/$USERNAME/.bashrc \
    && echo "unset PROMPT_COMMAND" >> /home/$USERNAME/.bashrc \
    && printf "export PS1=\"\\[\\033[01;32m\\]\\u@\\h\\[\\033[01;33m\\] \\w \\[\\033[01;31m\\]\\\$(__git_ps1 '(%%s)') \\n\\[\\033[01;34m\\]\\\\$ \\[\\033[00m\\]\"\n" >> /home/$USERNAME/.bashrc \
    && chmod a+x /usr/share/bash-completion/completions/git*

# 作業ディレクトリの設定
WORKDIR /workspace

# デフォルトユーザーの設定
USER $USERNAME

# bashrcを反映するためのシェル設定
SHELL ["/bin/bash", "-c"]

