/* eslint-disable */
import * as types from './graphql';
import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';

/**
 * Map of all GraphQL operations in the project.
 *
 * This map has several performance disadvantages:
 * 1. It is not tree-shakeable, so it will include all operations in the project.
 * 2. It is not minifiable, so the string of a GraphQL query will be multiple times inside the bundle.
 * 3. It does not support dead code elimination, so it will add unused operations.
 *
 * Therefore it is highly recommended to use the babel or swc plugin for production.
 * Learn more about it here: https://the-guild.dev/graphql/codegen/plugins/presets/preset-client#reducing-bundle-size
 */
const documents = {
    "mutation ScoreResume($file: Upload!, $job: String!) {\n  scoreResume(resume: $file, jobDesc: $job) {\n    resumeEval {\n      overallComment\n      education {\n        alignment\n        comment\n      }\n      experience {\n        depth\n        impact\n        relevance\n        comment\n      }\n      leadership {\n        depth\n        impact\n        relevance\n        comment\n      }\n      projects {\n        depth\n        impact\n        relevance\n        comment\n      }\n      research {\n        depth\n        impact\n        relevance\n        comment\n      }\n      skills {\n        alignment\n        comment\n      }\n    }\n    resumeWeights {\n      education\n      experience\n      projects\n      leadership\n      research\n      skills\n      reasoning\n    }\n    finalScore\n  }\n}": types.ScoreResumeDocument,
};

/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 *
 *
 * @example
 * ```ts
 * const query = gql(`query GetUser($id: ID!) { user(id: $id) { name } }`);
 * ```
 *
 * The query argument is unknown!
 * Please regenerate the types.
 */
export function gql(source: string): unknown;

/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function gql(source: "mutation ScoreResume($file: Upload!, $job: String!) {\n  scoreResume(resume: $file, jobDesc: $job) {\n    resumeEval {\n      overallComment\n      education {\n        alignment\n        comment\n      }\n      experience {\n        depth\n        impact\n        relevance\n        comment\n      }\n      leadership {\n        depth\n        impact\n        relevance\n        comment\n      }\n      projects {\n        depth\n        impact\n        relevance\n        comment\n      }\n      research {\n        depth\n        impact\n        relevance\n        comment\n      }\n      skills {\n        alignment\n        comment\n      }\n    }\n    resumeWeights {\n      education\n      experience\n      projects\n      leadership\n      research\n      skills\n      reasoning\n    }\n    finalScore\n  }\n}"): (typeof documents)["mutation ScoreResume($file: Upload!, $job: String!) {\n  scoreResume(resume: $file, jobDesc: $job) {\n    resumeEval {\n      overallComment\n      education {\n        alignment\n        comment\n      }\n      experience {\n        depth\n        impact\n        relevance\n        comment\n      }\n      leadership {\n        depth\n        impact\n        relevance\n        comment\n      }\n      projects {\n        depth\n        impact\n        relevance\n        comment\n      }\n      research {\n        depth\n        impact\n        relevance\n        comment\n      }\n      skills {\n        alignment\n        comment\n      }\n    }\n    resumeWeights {\n      education\n      experience\n      projects\n      leadership\n      research\n      skills\n      reasoning\n    }\n    finalScore\n  }\n}"];

export function gql(source: string) {
  return (documents as any)[source] ?? {};
}

export type DocumentType<TDocumentNode extends DocumentNode<any, any>> = TDocumentNode extends DocumentNode<  infer TType,  any>  ? TType  : never;