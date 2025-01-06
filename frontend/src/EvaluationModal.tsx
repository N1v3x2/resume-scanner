import { ScoreResumeMutation } from "./__generated__/types";

interface EvaluationModalProps {
  resumeEval: ScoreResumeMutation;
  onClose: () => void;
}

export default function EvaluationModal({
  resumeEval,
  onClose,
}: EvaluationModalProps) {
  return (
    <div className="fixed top-0 left-0 w-screen h-screen bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white min-w-[800px] w-1/2 h-5/6 py-4 text-black flex flex-col gap-4 overflow-scroll">
        <section className="flex justify-between items-center px-6">
          <h1 className="text-2xl font-semibold">Resume Evaluation</h1>
          <button
            className="text-lg px-6 py-1 bg-red-500 hover:bg-red-700 text-white rounded-md"
            onClick={() => onClose()}
          >
            Close
          </button>
        </section>
        <hr />
        <div className="px-6 flex flex-col gap-4">
          <section className="flex flex-col gap-2">
            <h1 className="text-2xl font-semibold">Scores</h1>
            <em>
              Scores and weights are LLM-generated based on the provided job
              description and resume.
            </em>
            <table className="table-auto mb-0 border-2 border-zinc-500">
              <thead>
                <tr className="*:px-2 *:py-1 bg-zinc-700 text-white">
                  <th className="text-left">Section</th>
                  <th className="text-right">Weight</th>
                  <th className="text-right">Unweighted Score</th>
                  <th className="text-right">Weighted Score</th>
                </tr>
              </thead>
              <tbody>
                <tr className="*:px-2 *:py-1 odd:bg-white even:bg-zinc-100">
                  <td>Education</td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      resumeEval.scoreResume.resumeWeights.education * 100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      (resumeEval.scoreResume.resumeEval.education.alignment /
                        5) *
                      100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeWeights.education *
                        resumeEval.scoreResume.resumeEval.education.alignment) /
                        5) *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                </tr>
                <tr className="*:px-2 *:py-1 odd:bg-white even:bg-zinc-100">
                  <td>Experience</td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      resumeEval.scoreResume.resumeWeights.experience * 100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.experience.depth +
                        resumeEval.scoreResume.resumeEval.experience.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.experience.relevance /
                        5) *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.experience.depth +
                        resumeEval.scoreResume.resumeEval.experience.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.experience.relevance /
                        5) *
                      resumeEval.scoreResume.resumeWeights.experience *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                </tr>
                <tr className="*:px-2 *:py-1 odd:bg-white even:bg-zinc-100">
                  <td>Projects</td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      resumeEval.scoreResume.resumeWeights.projects * 100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.projects.depth +
                        resumeEval.scoreResume.resumeEval.projects.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.projects.relevance /
                        5) *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.projects.depth +
                        resumeEval.scoreResume.resumeEval.projects.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.projects.relevance /
                        5) *
                      resumeEval.scoreResume.resumeWeights.projects *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                </tr>
                <tr className="*:px-2 *:py-1 odd:bg-white even:bg-zinc-100">
                  <td>Leadership</td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      resumeEval.scoreResume.resumeWeights.leadership * 100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.leadership.depth +
                        resumeEval.scoreResume.resumeEval.leadership.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.leadership.relevance /
                        5) *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.leadership.depth +
                        resumeEval.scoreResume.resumeEval.leadership.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.leadership.relevance /
                        5) *
                      resumeEval.scoreResume.resumeWeights.leadership *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                </tr>
                <tr className="*:px-2 *:py-1 odd:bg-white even:bg-zinc-100">
                  <td>Research</td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      resumeEval.scoreResume.resumeWeights.research * 100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.research.depth +
                        resumeEval.scoreResume.resumeEval.research.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.research.relevance /
                        5) *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeEval.research.depth +
                        resumeEval.scoreResume.resumeEval.research.impact) /
                        10) *
                      (resumeEval.scoreResume.resumeEval.research.relevance /
                        5) *
                      resumeEval.scoreResume.resumeWeights.research *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                </tr>
                <tr className="*:px-2 *:py-1 odd:bg-white even:bg-zinc-100">
                  <td>Skills</td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      resumeEval.scoreResume.resumeWeights.skills * 100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      (resumeEval.scoreResume.resumeEval.skills.alignment / 5) *
                      100
                    ).toFixed(0)}
                    %
                  </td>
                  <td className="text-right border-l-2 border-zinc-500">
                    {(
                      ((resumeEval.scoreResume.resumeWeights.skills *
                        resumeEval.scoreResume.resumeEval.skills.alignment) /
                        5) *
                      100
                    ).toFixed(1)}
                    %
                  </td>
                </tr>
                <tr className="*:py-1 *:px-2 font-bold">
                  <td className="text-left border-t-2 border-zinc-500">
                    Overall
                  </td>
                  <td className="text-left border-t-2 border-zinc-500"></td>
                  <td className="text-left border-t-2 border-zinc-500"></td>
                  <td className="text-right border-t-2 border-l-2 border-zinc-500">
                    {(resumeEval.scoreResume.finalScore * 100).toFixed(1)}%
                  </td>
                </tr>
              </tbody>
            </table>
          </section>
          <hr />
          <section>
            <h1 className="text-2xl font-semibold">Overall Feedback</h1>
            <p>{resumeEval.scoreResume.resumeEval.overallComment}</p>
          </section>

          <section className="ml-4">
            <h2 className="text-xl font-semibold">Education</h2>
            <p>{resumeEval.scoreResume.resumeEval.education.comment}</p>
          </section>

          <section className="ml-4">
            <h2 className="text-xl font-semibold">Experience</h2>
            <p>{resumeEval.scoreResume.resumeEval.experience.comment}</p>
          </section>

          <section className="ml-4">
            <h2 className="text-xl font-semibold">Projects</h2>
            <p>{resumeEval.scoreResume.resumeEval.projects.comment}</p>
          </section>

          <section className="ml-4">
            <h2 className="text-xl font-semibold">Leadership</h2>
            <p>{resumeEval.scoreResume.resumeEval.leadership.comment}</p>
          </section>

          <section className="ml-4">
            <h2 className="text-xl font-semibold">Research</h2>
            <p>{resumeEval.scoreResume.resumeEval.research.comment}</p>
          </section>

          <section className="ml-4">
            <h2 className="text-xl font-semibold">Skills</h2>
            <p>{resumeEval.scoreResume.resumeEval.skills.comment}</p>
          </section>
        </div>
      </div>
    </div>
  );
}
