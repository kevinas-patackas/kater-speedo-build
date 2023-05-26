module.exports = {
  apps: [
    {
      name: "server",
      cwd: "/kater-speedo-build",
      script: "node",
      args: "server/main.js",
      env: {
        LOG_ALL: "false",
        LOG_GPSD: "false",
        LOG_TEMPERATURE: "false",
        LOG_RPM: "false",
        LOG_FUEL: "false",
        LOG_TRIM: "false",
        LOG_VOLTAGE: "false",
        LOG_OIL_PRESSURE: "false",
      },
    },
    {
      name: "client",
      cwd: "/kater-speedo-build",
      script: "serve",
      args: "client -p 4200",
    },
  ],
};
