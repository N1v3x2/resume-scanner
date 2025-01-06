import { gql } from '@apollo/client';
import * as Apollo from '@apollo/client';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type MakeEmpty<T extends { [key: string]: unknown }, K extends keyof T> = { [_ in K]?: never };
export type Incremental<T> = T | { [P in keyof T]?: P extends ' $fragmentName' | '__typename' ? T[P] : never };
const defaultOptions = {} as const;
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


export const ScoreResumeDocument = gql`
    mutation ScoreResume($file: Upload!, $job: String!) {
  scoreResume(resume: $file, jobDesc: $job) {
    resumeEval {
      overallComment
      education {
        alignment
        comment
      }
      experience {
        depth
        impact
        relevance
        comment
      }
      leadership {
        depth
        impact
        relevance
        comment
      }
      projects {
        depth
        impact
        relevance
        comment
      }
      research {
        depth
        impact
        relevance
        comment
      }
      skills {
        alignment
        comment
      }
    }
    resumeWeights {
      education
      experience
      projects
      leadership
      research
      skills
      reasoning
    }
    finalScore
  }
}
    `;
export type ScoreResumeMutationFn = Apollo.MutationFunction<ScoreResumeMutation, ScoreResumeMutationVariables>;

/**
 * __useScoreResumeMutation__
 *
 * To run a mutation, you first call `useScoreResumeMutation` within a React component and pass it any options that fit your needs.
 * When your component renders, `useScoreResumeMutation` returns a tuple that includes:
 * - A mutate function that you can call at any time to execute the mutation
 * - An object with fields that represent the current status of the mutation's execution
 *
 * @param baseOptions options that will be passed into the mutation, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options-2;
 *
 * @example
 * const [scoreResumeMutation, { data, loading, error }] = useScoreResumeMutation({
 *   variables: {
 *      file: // value for 'file'
 *      job: // value for 'job'
 *   },
 * });
 */
export function useScoreResumeMutation(baseOptions?: Apollo.MutationHookOptions<ScoreResumeMutation, ScoreResumeMutationVariables>) {
        const options = {...defaultOptions, ...baseOptions}
        return Apollo.useMutation<ScoreResumeMutation, ScoreResumeMutationVariables>(ScoreResumeDocument, options);
      }
export type ScoreResumeMutationHookResult = ReturnType<typeof useScoreResumeMutation>;
export type ScoreResumeMutationResult = Apollo.MutationResult<ScoreResumeMutation>;
export type ScoreResumeMutationOptions = Apollo.BaseMutationOptions<ScoreResumeMutation, ScoreResumeMutationVariables>;