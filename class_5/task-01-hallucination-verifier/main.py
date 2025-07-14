#!/usr/bin/env python3
"""
Main demonstration script for Task 05 - Hallucination Verifier
"""

import os
import json
from solution import verify_hallucination, evaluate_hallucination_detection, llm_as_judge_evaluation

def main():
    print("🔍 Hallucination Verifier Demo")
    print("=" * 50)
    
    # Demo questions
    demo_questions = [
        "Who was the first person to walk on Mars?",
        "What is the capital of France?",
        "Who invented the computer mouse?",
        "What is the population of the planet Jupiter?"
    ]
    
    for i, question in enumerate(demo_questions, 1):
        print(f"\n📝 Question {i}: {question}")
        print("-" * 40)
        
        result = verify_hallucination(question)
        
        print(f"💬 Answer: {result['answer']}")
        print(f"📚 Sources: {result['sources']}")
        print(f"🎯 Is Hallucination: {result['is_hallucination']}")
        print(f"📊 Confidence: {result['confidence']:.2f}")
        print(f"🧠 Reasoning: {result['reasoning']}")
        
    print("\n" + "=" * 50)
    print("Demo completed! ✅")

def evaluation_demo():
    """Demonstrate comprehensive evaluation capabilities."""
    print("\n🧪 Evaluation Demo")
    print("=" * 50)
    
    # Load test questions from sample data
    test_questions = []
    try:
        with open('sample_questions.jsonl', 'r') as f:
            for line in f:
                test_questions.append(json.loads(line.strip()))
    except FileNotFoundError:
        # Fallback test questions
        test_questions = [
            {"question": "Who was the first person to walk on Mars?", "expected_hallucination": True},
            {"question": "What is the capital of France?", "expected_hallucination": False},
            {"question": "Who invented the computer mouse?", "expected_hallucination": False},
            {"question": "What is the population of the planet Jupiter?", "expected_hallucination": True}
        ]
    
    print(f"📊 Running evaluation on {len(test_questions)} questions...")
    
    # Basic accuracy evaluation
    print("\n1️⃣ Basic Accuracy Evaluation")
    print("-" * 30)
    basic_results = evaluate_hallucination_detection(test_questions)
    print(f"✅ Accuracy: {basic_results['accuracy']:.2%}")
    print(f"📈 Correct: {basic_results['correct']}/{basic_results['total']}")
    
    # LLM-as-Judge comprehensive evaluation
    print("\n2️⃣ LLM-as-Judge Comprehensive Evaluation")
    print("-" * 30)
    print("🤖 Running comprehensive analysis...")
    
    llm_results = llm_as_judge_evaluation(test_questions)
    
    print(f"\n🏆 Performance Level: {llm_results['performance_level']}")
    print(f"🎯 Binary Accuracy: {llm_results['binary_accuracy']:.2%}")
    print(f"📊 Average Scores (0-10 scale):")
    print(f"   • Output Accuracy: {llm_results['avg_output_accuracy']:.1f}")
    print(f"   • Reasoning Quality: {llm_results['avg_reasoning_quality']:.1f}")
    print(f"   • Source Quality: {llm_results['avg_source_quality']:.1f}")
    print(f"   • Process Methodology: {llm_results['avg_process_methodology']:.1f}")
    print(f"   • Confidence Calibration: {llm_results['avg_confidence_calibration']:.1f}")
    print(f"   • Overall Assessment: {llm_results['avg_overall_assessment']:.1f}")
    
    print("\n💡 Evaluation Insights:")
    if llm_results['avg_overall_assessment'] >= 8.0:
        print("   🌟 Excellent performance! The system demonstrates superior hallucination detection.")
    elif llm_results['avg_overall_assessment'] >= 6.5:
        print("   👍 Good performance with room for fine-tuning prompting techniques.")
    elif llm_results['avg_overall_assessment'] >= 5.0:
        print("   ⚠️  Adequate performance but consider improving source verification.")
    else:
        print("   🔧 Needs improvement in methodology and prompt engineering.")

if __name__ == "__main__":
    # Check for required API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key and try again.")
        exit(1)
    
    # Run main demo
    main()
    
    # Run evaluation demo
    evaluation_demo() 