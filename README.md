# gold-timeseries-tracker (API + Time-Series Tracker)
A Python tool that automatically collects daily gold price data, tracks trends, and builds a long-term time-series dataset.

## Overview

This project is a Python-based automation tool that retrieves daily gold market data and stores it in a long-term time-series dataset.
It is designed to run repeatedly (daily or hourly) and build a structured historical record that can later be used for analysis, trend detection, and decision-making.

## Why I Built This

Most financial websites only show gold prices for the current day or in short windows, making it difficult to track meaningful changes over time.
This tool solves the problem by automatically collecting and storing gold market data every day, so I can analyse price trends, momentum, and volatility without manually checking or copying data.

## What Problem This Solves

It automates the long-term collection of gold market data so users can track trends, detect momentum shifts, and build their own historical dataset without relying on external platforms.

## What Data Will Be Tracked

The following metrics are collected each day:

- Daily closing price

- Daily % change

- EMA-21 vs SMA-5 direction signal (EMA-21 above or below SMA-5)

- Volatility — measured as the daily high–low range

- Momentum signal — whether the price closed above or below the 7-day moving average

## Features (Planned & In Progress)
✔ Daily Data Retrieval

Automatically pulls daily gold price data from a public API.

✔ Time-Series Storage

Appends each new data point to a local dataset (JSON/CSV).

✔ Technical Indicators

Calculates basic trend indicators including:

- EMA-21

- SMA-5

- 7-day moving average

- High–low volatility

✔ Trend Signals

Evaluates whether the gold market is gaining or losing momentum.

🔄 Scheduled Execution (Planned)

Integration with task schedulers (Windows Task Scheduler / cron) to run automatically once per day.

🔄 Dashboard (Future Work)

Optional dashboard for visualising the time-series trends.

## Technologies Used

Python

Requests (for API calls)

Pandas

JSON/CSV storage

Simple moving-average calculations

## Project Status
In progress.

Data collection logic will be implemented first, followed by indicator calculations, and finally scheduling and optional dashboards.