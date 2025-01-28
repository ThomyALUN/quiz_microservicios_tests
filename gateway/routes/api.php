<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\BandController;
use App\Http\Controllers\GenreController;
use App\Http\Controllers\LabelController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::prefix('/bands')->group(function () {
    Route::get('/', [BandController::class, 'index']);
    Route::get('/{id}', [BandController::class, 'show']);
});

Route::prefix('/genres')->group(function () {
    Route::get('/', [GenreController::class, 'index']);
    Route::get('/{id}', [GenreController::class, 'show']);
});

Route::post('/generate_labels', [LabelController::class, 'generate_labels']);
Route::get('/record_labels', [LabelController::class, 'get_record_labels']);