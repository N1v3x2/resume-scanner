import { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  schema: "http://localhost:8000/graphql",
  documents: ["src/graphql/**/*.graphql"],
  generates: {
    "./src/__generated__/types.ts": {
      plugins: [
        "typescript",
        "typescript-operations",
        "typescript-react-apollo"
      ],
      config: {
        avoidOptionals: true,
        skipTypename: true
      }
    }
  }
};

export default config;