"""
Inference Demo: Running predictions with trained AzureML models

This script demonstrates how to load and use models trained in AzureML
for making predictions locally.

Usage:
    # Custom trained model (joblib)
    python inference_demo.py --model-path ./downloads/JOB_NAME/outputs/model.joblib
    
    # AutoML model (MLflow format - directory)
    python inference_demo.py --model-path ./downloads/JOB_NAME/outputs/mlflow-model
    
    # AutoML model (pickle file)
    python inference_demo.py --model-path ./downloads/JOB_NAME/outputs/model.pkl
"""


import argparse
from pathlib import Path
from typing import Any, Optional, Union

import joblib
import pandas as pd


def create_sample_data() -> pd.DataFrame:
    """Create sample car data for prediction.
    
    Note: This creates data matching the full AutoML model signature.
    If your model was trained with fewer features (e.g., from train.py),
    you may need to adjust this to match those features only.
    """
    return pd.DataFrame({
        'Path': ['path/to/car1', 'path/to/car2', 'path/to/car3', 'path/to/car4'],
        'name': ['Maruti Swift', 'Hyundai Creta', 'Honda City', 'Toyota Innova'],
        'year': [2015, 2018, 2012, 2020],
        'km_driven': [50000, 30000, 80000, 15000],
        'fuel': ['Petrol', 'Diesel', 'Petrol', 'Diesel'],
        'seller_type': ['Individual', 'Dealer', 'Individual', 'Dealer'],
        'transmission': ['Manual', 'Manual', 'Automatic', 'Automatic'],
        'owner': ['First Owner', 'First Owner', 'Second Owner', 'First Owner'],
        'mileage': ['19.1 kmpl', '21.4 kmpl', '17.8 kmpl', '14.3 kmpl'],
        'engine': ['1197 CC', '1493 CC', '1497 CC', '2393 CC'],
        'max_power': ['81.80 bhp', '113.4 bhp', '117.3 bhp', '138.8 bhp'],
        'torque': ['113Nm@ 4200rpm', '250Nm@ 1500-2750rpm', '145Nm@ 4600rpm', '343Nm@ 1400-2600rpm'],
        'seats': [5.0, 5.0, 5.0, 7.0]
    })


def load_model(model_path: str) -> Any:
    """Load a trained model from disk (supports joblib, pickle, and MLflow)."""
    path = Path(model_path)
    if not path.exists():
        raise FileNotFoundError(f"Model not found at: {model_path}")
    
    print(f"Loading model from: {model_path}")
    
    # If it's a directory, try MLflow first
    if path.is_dir():
        try:
            import mlflow
            print("  → Detected MLflow model directory")
            model = mlflow.pyfunc.load_model(str(path))
            print("  → Loaded as MLflow model")
            return model
        except ImportError:
            print("  → MLflow not installed. Install with: pip install mlflow")
            raise
        except Exception as e:
            print(f"  → Failed to load as MLflow: {e}")
            raise
    
    # If it's a file, try joblib/pickle
    if path.suffix in ['.joblib', '.pkl', '.pickle']:
        try:
            model = joblib.load(path)
            print(f"  → Loaded as {path.suffix} file")
            return model
        except Exception as e:
            print(f"  → Failed to load with joblib: {e}")
            raise
    
    # Unknown format
    raise ValueError(f"Unsupported model format: {path}. Expected .joblib, .pkl, or MLflow directory")


def run_inference(model: Any, data: pd.DataFrame) -> Union[pd.Series, pd.DataFrame, Any]:
    """Run predictions on the provided data."""
    print("\n" + "="*60)
    print("INPUT DATA:")
    print("="*60)
    print(data.to_string(index=False))
    
    print("\n" + "="*60)
    print("PREDICTIONS:")
    print("="*60)
    
    # Both MLflow and sklearn models support .predict()
    predictions = model.predict(data)
    
    # Display results
    results = data.copy()
    results['predicted_price'] = predictions
    
    for idx, row in results.iterrows():
        car_name = row.get('name', f"{row['year']} {row['fuel']} car")
        print(f"\n{idx + 1}. {car_name} ({row['km_driven']:,} km)")
        print(f"   Year: {row['year']}, Transmission: {row['transmission']}, Owner: {row['owner']}")
        print(f"   Seller Type: {row['seller_type']}")
        print(f"   → Predicted Price: ₹{row['predicted_price']:,.2f}")
    
    print("\n" + "="*60)
    return predictions


def main() -> None:
    parser = argparse.ArgumentParser(description="Run inference with trained AzureML models")
    parser.add_argument(
        "--model-path",
        required=True,
        help="Path to model file (.joblib, .pkl) or MLflow model directory"
    )
    parser.add_argument(
        "--data",
        help="Optional: Path to CSV file with custom test data"
    )
    
    args = parser.parse_args()
    
    # Load the model
    try:
        model = load_model(args.model_path)
        print(f"✓ Model loaded successfully")
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        return
    
    # Prepare test data
    if args.data:
        print(f"\nLoading custom data from: {args.data}")
        test_data = pd.read_csv(args.data)
    else:
        print("\nUsing sample test data...")
        test_data = create_sample_data()
    
    # Run inference
    try:
        predictions = run_inference(model, test_data)
        print("\n✓ Inference completed successfully!")
        print(f"\nTotal predictions: {len(predictions)}")
        print(f"Price range: ₹{predictions.min():,.2f} - ₹{predictions.max():,.2f}")
        print(f"Average predicted price: ₹{predictions.mean():,.2f}")
    except Exception as e:
        print(f"\n✗ Error during inference: {e}")
        print("\nTroubleshooting:")
        print("- Ensure the model was trained with the same features")
        print("- Check that all required columns are present in the test data")
        print("- Verify the model file is not corrupted")
        
        # Try to show what features the model expects
        error_msg = str(e)
        if "missing inputs" in error_msg.lower():
            print("\n💡 TIP: Your model may have been trained on the FULL dataset")
            print("   with all 13 features. The sample data has been updated to")
            print("   include: Path, name, mileage, engine, max_power, torque, seats")
            print("\n   If you trained with train.py (only 6 features), you may need")
            print("   to download a model from that job instead.")


if __name__ == "__main__":
    main()
