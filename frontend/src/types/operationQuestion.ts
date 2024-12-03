/**
 * 一般ユーザーの問題関連の操作に関する型定義
 */
// 問題作成
export type PostCreate = {
  step: number;
  question: string;
  // question_image:string,
  correct_option: string;
  wrong_option_1: string;
  wrong_option_2: string;
  explanation: string;
  // explanation_image:string,
  user_id: number | string | null;
  category_name: string;
};

// 問題編集
export type PostEdit = {
  step: number;
  question: string;
  // question_image:string,
  correct_option: string;
  wrong_option_1: string;
  wrong_option_2: string;
  explanation: string;
  // explanation_image:string,
  category_name: string;
};

/**
 * 管理者の操作に関する型定義
 */
// 問題編集（）
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

// 編集してPostする問題（管理者）
export type PostFeedback = {
  id: number | string;
  difficulty: number;
  is_accept: boolean;
  step: number | string;
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
