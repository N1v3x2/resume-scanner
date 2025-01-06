/* eslint-disable */
import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type MakeEmpty<T extends { [key: string]: unknown }, K extends keyof T> = { [_ in K]?: never };
export type Incremental<T> = T | { [P in keyof T]?: P extends ' $fragmentName' | '__typename' ? T[P] : never };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: { input: string; output: string; }
  String: { input: string; output: string; }
  Boolean: { input: boolean; output: boolean; }
  Int: { input: number; output: number; }
  Float: { input: number; output: number; }
  Upload: { input: any; output: any; }
};

export type Mutation = {
  __typename?: 'Mutation';
  scoreResume: ScoredResumeType;
};


export type MutationScoreResumeArgs = {
  jobDesc: Scalars['String']['input'];
  resume: Scalars['Upload']['input'];
};

export type Query = {
  __typename?: 'Query';
  placeholder: Scalars['String']['output'];
};

export type ReducedSectionScoreType = {
  __typename?: 'ReducedSectionScoreType';
  /** Alignment score (0-5) */
  alignment: Scalars['Int']['output'];
  /** Explanation for the score in this section */
  comment: Scalars['String']['output'];
};

export type ResumeEvaluationType = {
  __typename?: 'ResumeEvaluationType';
  education: ReducedSectionScoreType;
  experience: SectionScoreType;
  leadership: SectionScoreType;
  /** General comments about the resume, including strengths and weaknesses */
  overallComment: Scalars['String']['output'];
  projects: SectionScoreType;
  research: SectionScoreType;
  skills: ReducedSectionScoreType;
};

export type ResumeWeightsType = {
  __typename?: 'ResumeWeightsType';
  education: Scalars['Float']['output'];
  experience: Scalars['Float']['output'];
  leadership: Scalars['Float']['output'];
  projects: Scalars['Float']['output'];
  reasoning: Scalars['String']['output'];
  research: Scalars['Float']['output'];
  skills: Scalars['Float']['output'];
  validation: Scalars['String']['output'];
};

export type ScoredResumeType = {
  __typename?: 'ScoredResumeType';
  finalScore: Scalars['Float']['output'];
  resumeEval: ResumeEvaluationType;
  resumeWeights: ResumeWeightsType;
};

export type SectionScoreType = {
  __typename?: 'SectionScoreType';
  /** Explanation for the scores in this section */
  comment: Scalars['String']['output'];
  /** Depth score (0-5) */
  depth: Scalars['Int']['output'];
  /** Impact score (0-5) */
  impact: Scalars['Int']['output'];
  /** Relevance score (0-5) */
  relevance: Scalars['Int']['output'];
};

export type ScoreResumeMutationVariables = Exact<{
  file: Scalars['Upload']['input'];
  job: Scalars['String']['input'];
}>;


export type ScoreResumeMutation = { __typename?: 'Mutation', scoreResume: { __typename?: 'ScoredResumeType', finalScore: number, resumeEval: { __typename?: 'ResumeEvaluationType', overallComment: string, education: { __typename?: 'ReducedSectionScoreType', alignment: number, comment: string }, experience: { __typename?: 'SectionScoreType', depth: number, impact: number, relevance: number, comment: string }, leadership: { __typename?: 'SectionScoreType', depth: number, impact: number, relevance: number, comment: string }, projects: { __typename?: 'SectionScoreType', depth: number, impact: number, relevance: number, comment: string }, research: { __typename?: 'SectionScoreType', depth: number, impact: number, relevance: number, comment: string }, skills: { __typename?: 'ReducedSectionScoreType', alignment: number, comment: string } }, resumeWeights: { __typename?: 'ResumeWeightsType', education: number, experience: number, projects: number, leadership: number, research: number, skills: number, reasoning: string } } };


export const ScoreResumeDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"ScoreResume"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"file"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"Upload"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"job"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"scoreResume"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"resume"},"value":{"kind":"Variable","name":{"kind":"Name","value":"file"}}},{"kind":"Argument","name":{"kind":"Name","value":"jobDesc"},"value":{"kind":"Variable","name":{"kind":"Name","value":"job"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"resumeEval"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"overallComment"}},{"kind":"Field","name":{"kind":"Name","value":"education"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"alignment"}},{"kind":"Field","name":{"kind":"Name","value":"comment"}}]}},{"kind":"Field","name":{"kind":"Name","value":"experience"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"depth"}},{"kind":"Field","name":{"kind":"Name","value":"impact"}},{"kind":"Field","name":{"kind":"Name","value":"relevance"}},{"kind":"Field","name":{"kind":"Name","value":"comment"}}]}},{"kind":"Field","name":{"kind":"Name","value":"leadership"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"depth"}},{"kind":"Field","name":{"kind":"Name","value":"impact"}},{"kind":"Field","name":{"kind":"Name","value":"relevance"}},{"kind":"Field","name":{"kind":"Name","value":"comment"}}]}},{"kind":"Field","name":{"kind":"Name","value":"projects"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"depth"}},{"kind":"Field","name":{"kind":"Name","value":"impact"}},{"kind":"Field","name":{"kind":"Name","value":"relevance"}},{"kind":"Field","name":{"kind":"Name","value":"comment"}}]}},{"kind":"Field","name":{"kind":"Name","value":"research"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"depth"}},{"kind":"Field","name":{"kind":"Name","value":"impact"}},{"kind":"Field","name":{"kind":"Name","value":"relevance"}},{"kind":"Field","name":{"kind":"Name","value":"comment"}}]}},{"kind":"Field","name":{"kind":"Name","value":"skills"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"alignment"}},{"kind":"Field","name":{"kind":"Name","value":"comment"}}]}}]}},{"kind":"Field","name":{"kind":"Name","value":"resumeWeights"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"education"}},{"kind":"Field","name":{"kind":"Name","value":"experience"}},{"kind":"Field","name":{"kind":"Name","value":"projects"}},{"kind":"Field","name":{"kind":"Name","value":"leadership"}},{"kind":"Field","name":{"kind":"Name","value":"research"}},{"kind":"Field","name":{"kind":"Name","value":"skills"}},{"kind":"Field","name":{"kind":"Name","value":"reasoning"}}]}},{"kind":"Field","name":{"kind":"Name","value":"finalScore"}}]}}]}}]} as unknown as DocumentNode<ScoreResumeMutation, ScoreResumeMutationVariables>;