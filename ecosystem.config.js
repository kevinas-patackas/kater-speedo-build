module.exports = {
  apps: [
    {
      name: "server",
      cwd: "/kater-speedo-build",
      script: "node",
      args: "server/main.js",
    },
    {
      name: "client",
      cwd: "/kater-speedo-build",
      script: "serve",
      args: "client -p 4200",
    },
    {
      name: "chromium",
      cwd: "/path/to/kater-speedo-build",
      script: "chromium-browser",
      args: "--start-fullscreen http://localhost:4200",
      exec_interpreter: "none",
      exec_mode: "fork",
    },
  ],
};
