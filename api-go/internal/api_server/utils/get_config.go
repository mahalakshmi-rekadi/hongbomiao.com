package utils

import (
	"github.com/joho/godotenv"
	"os"
)

type Config struct {
	AppEnv                       string
	Port                         string
	GRPCServerHost               string
	GRPCServerPort               string
	OPAHost                      string
	OPAPort                      string
	DgraphHost                   string
	DgraphGRPCPort               string
	OpenCensusAgentHost          string
	OpenCensusAgentPort          string
	JaegerURL                    string
	EnableOpenTelemetryStdoutLog string

	JWTSecret string
}

func GetConfig() *Config {
	path := "config/api_server/"

	appEnv := os.Getenv("APP_ENV")
	if appEnv == "" {
		appEnv = "development"
	}

	_ = godotenv.Load(path + ".env." + appEnv + ".local")
	_ = godotenv.Load(path + ".env." + appEnv)

	return &Config{
		AppEnv:                       appEnv,
		Port:                         os.Getenv("PORT"),
		GRPCServerHost:               os.Getenv("GRPC_SERVER_HOST"),
		GRPCServerPort:               os.Getenv("GRPC_SERVER_PORT"),
		OPAHost:                      os.Getenv("OPA_HOST"),
		OPAPort:                      os.Getenv("OPA_PORT"),
		DgraphHost:                   os.Getenv("DGRAPH_HOST"),
		DgraphGRPCPort:               os.Getenv("DGRAPH_GRPC_PORT"),
		OpenCensusAgentHost:          os.Getenv("OPEN_CENSUS_AGENT_HOST"),
		OpenCensusAgentPort:          os.Getenv("OPEN_CENSUS_AGENT_PORT"),
		JaegerURL:                    os.Getenv("JAEGER_URL"),
		JWTSecret:                    os.Getenv("JWT_SECRET"),
		EnableOpenTelemetryStdoutLog: os.Getenv("ENABLE_OPEN_TELEMETRY_STDOUT_LOG"),
	}
}
