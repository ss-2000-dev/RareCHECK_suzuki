// 問題編集（管理者）

export type GetQuestionDetailAdmin = {
  id: number;
  difficulty: number;
  is_accept: boolean;
  step: number;
  category_name: string;
  question: string;
  // question_image: string;
  correct_option: string;
  wrong_option_1: string;
  wrong_option_2: string;
  explanation: string;
  // explanation_image: string;
  comment: string;
};
